from flask import Flask, render_template, request, jsonify
import json
import random
import components
import game_engine
 
app = Flask(__name__)

#ROUTE_FILE = "C:/Users/finng/Documents/Yr 11/Computer Science/Coding/Uni/Semester 1/Programming workshops/coursework 2/prog-coursewokr-main/"
ROUTE_FILE = "H:/git/Battleships-Coursework/prog-coursewokr-main/"

board = components.initialise_board()
battleships = components.create_battleships()

@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    """Allows the user to place their battleships on the web inteface

    Returns:
        The parameters to render
    """
    
    if request.method == 'GET':
        return render_template('placement.html', ships=battleships, board_size=10)
    
    elif request.method == 'POST':
        ship_data = request.get_json()
        with open(ROUTE_FILE + 'placement.json', 'w') as json_file:
            json.dump(ship_data, json_file) 
        global player_board
        player_board = components.place_battleships(board, battleships)
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
    ai_game_board = components.place_battleships(board=ai_board, ships=ai_ships, algorithm="random")
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

    hit = game_engine.attack(coordinates=coordinates, board=ai_game_board, battleships=battleships)
    #Use the coords to attack the AI board (generate the board in root function)

    finished = True
    for value in battleships.values():
            if value != '0': #Only run when all dict values are 0
                finished = False     
    if finished:
        return jsonify({'hit': hit, 'AI_turn': (0,0), 'finished':"Game over"})
    #AI_turh: generate_attack(maybe params i dont know)
    else:
        random_x = random.randrange(0, len(board))
        random_y = random.randrange(0,len(board))
        return jsonify({'hit': hit, 'AI_turn': (random_x,random_y), 'log':"Attacked and hit"})

if __name__ == '__main__':
    app.run()