from flask import Flask, render_template, request, jsonify
import json
import random
from components import initialise_board, place_battleships, create_battleships
from game_engine import attack
 
app = Flask(__name__)


board = initialise_board()
battleships = create_battleships()

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
        with open("C:/Users/finng/Documents/Yr 11/Computer Science/Coding/Uni/Semester 1/Programming workshops/coursework 2/prog-coursewokr-main/" + 'placement.json', 'w') as json_file:
            json.dump(ship_data, json_file) 
        global player_board
        player_board = place_battleships(board, battleships)
        return jsonify({'message': 'Received'}), 200 

@app.route('/', methods=['GET'])
def root():
    """The main logic behind the main page

    Returns:
        The main html with the parameters it needs
    """
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

    hit = attack(coordinates=coordinates, board=player_board, battleships=battleships)
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