import json
'''import json to read json files'''

route_file = "C:/Users/finng/Documents/Yr 11/Computer Science/Coding/Uni/Semester 1/Programming workshops/coursework 2/prog-coursewokr-main/" 
#route_file = 

def initialise_board(size: int = 10) -> list:
    """Creates the board
    Args:
        size (int, optional): Size of the grid. Defaults to 10.
    Returns:
        list: Return a list of list of nones
    """
    board_list = [ [None for x in range(0, size)] for y in range(0, size)] #Produces a grid of x rows and x columns
    return board_list

def create_battleships(filename: str = "battleships.txt") -> dict:
    """Creates the battleships that can then later be placed
    Args:
        filename (str, optional): A file containing the battleships names and size. Defaults to "battleships.txt ".
    Returns:
        dict: _description_
    """
    
    battleships = {}
    with open(route_file + filename) as text_file:
        for line in text_file:
            line = line.strip()
            (key, val) = line.split(':')
            battleships[key] = int(val)
       
    #print(battleships) 
    return battleships


def place_battleships(board: list, ships: dict) -> list:
    """A function to place down the ships
    Args:
        board (list): Empty list of list from initialise_board
        ships (dict): Dictionary of ships from create_battleships
    Returns:
        list: _description_
    """
     
    with open(route_file + 'placement.json') as ship_data:
        data = json.load(ship_data) #convert the json into a useable foramt
        json_values = list(data.values()) #make a list of the json values
        json_keys = list(data.keys()) #make a list of the json keys
        
    for x in range(0, len(ships)):
        start_row = int(json_values[x][1]) #access the string stored in start x coord of json file for each ship and cast to int
        start_column = int(json_values[x][0])
        rotation = str(json_values[x][2]) #access the rotation from the json file for each ship and cast to string
        key = list(ships.keys())[x] #cast the ships key into a list
        value = list(ships.values())[x] #cast the ships values into a list
        if rotation == 'v':
            for i in range(0, int(value)):
                board[start_row + i][start_column] = [key] #only loop through the row to place vertically
        elif rotation == 'h':
            for j in range(0, int(value)):
                board[start_row][start_column + j] = [key] #only loop through the column to place horizontally
                
    return board


#board = initialise_board()
#ships = create_battleships()
#place_battleships(board, ships)
#
#for x in board:
#    print(x)
