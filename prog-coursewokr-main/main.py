from flask import Flask, render_template, request, jsonify
import json
import random
import components
import game_engine
import mp_game_engine
 
app = Flask(__name__)

#ROUTE_FILE = "D:/0000000 wrok/Uni/Semester 1/battleships colour/Battleships-Coursework/prog-coursewokr-main/"
#ROUTE_FILE = "H:/git/Battleships-Coursework/prog-coursewokr-main/"

board = components.initialise_board()
player_battleships = components.create_battleships()
ai_battleships = components.create_battleships()

@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    """Allows the user to place their battleships on the web inteface

    Returns:
        The parameters to render
    """
    
    if request.method == 'GET':
        return render_template('placement.html', ships=player_battleships, board_size=10)
    
    elif request.method == 'POST':
        ship_data = request.get_json()
        with open('placement.json', 'w') as json_file:
            json.dump(ship_data, json_file) 
        global player_board
        player_board = components.place_battleships(board, player_battleships)
        return jsonify({'message': 'Received'}), 200 

@app.route('/', methods=['GET'])
def root():
    """The main logic behind the main page

    Returns:
        The main html with the parameters it needs
    """
    global ai_game_board
    ai_board = components.initialise_board()
    ai_ships = components.create_battleships()
    ai_game_board = components.place_battleships(board=ai_board, ships=ai_ships, algorithm="random") #generates a board for the AI and globalises it
    if request.method == 'GET':
        return render_template('main.html', player_board=player_board, board_size = 10) #board should be an intilised board based on past function
    
@app.route('/attack', methods=['GET'])
def process_attack():
    """Allows the user to click on a square to attack it

    Returns:
        _type_: _description_
    """
    x = request.args.get('x')
    y = request.args.get('y')
    coordinates = (int(x),int(y))

    if ai_game_board[coordinates[0]][coordinates[1]] == "O" or ai_game_board[coordinates[0]][coordinates[1]] == "X":
        return json({'hit': False, 'AI_Turn': None}) #Stops the program from processing an attack if we have already attacked that square 
    hit = game_engine.attack(coordinates=coordinates, board=ai_game_board, battleships=ai_battleships)
    #Use the coords to attack the AI board

    ai_attack_coords = mp_game_engine.generate_attack(player_board)
    game_engine.attack(coordinates = ai_attack_coords, board = player_board, battleships=player_battleships)   
    
    no_ai_ships = all(value == "0" for value in ai_battleships.values())  
    no_player_ships = all(value == "0" for value in player_battleships.values())
            
            
    print(player_battleships) 
    print(ai_battleships)
    
    if no_ai_ships:
        return jsonify({'hit': hit, 'AI_Turn': ai_attack_coords, 'finished':"Game over, player wins!"})
    elif no_player_ships:
        return jsonify({'hit': hit, 'AI_Turn': ai_attack_coords, 'finished':"Game over, AI wins!"})
    else:
        return jsonify({'hit': hit, 'AI_Turn': ai_attack_coords, 'log':"Attacked and hit"})

if __name__ == '__main__':
    app.run()