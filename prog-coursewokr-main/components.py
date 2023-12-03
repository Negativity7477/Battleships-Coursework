import json
import random 
'''import json to read json files and random for random placement
'''

#ROUTE_FILE = "C:/Users/finng/Documents/Yr 11/Computer Science/Coding/Uni/Semester 1/Programming workshops/coursework 2/prog-coursewokr-main/" 
ROUTE_FILE = "H:/git/Battleships-Coursework/prog-coursewokr-main/"

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
    with open(ROUTE_FILE + filename) as text_file:
        for line in text_file:
            line = line.strip()
            (key, val) = line.split(':')
            battleships[key] = int(val)
       
    return battleships


def place_battleships(board: list, ships: dict, algorithm: str = "custom") -> list:
    """A function to place down the ships
    Args:
        board (list): Empty list of list from initialise_board
        ships (dict): Dictionary of ships from create_battleships
        algorithm (str): Allows the user to select how the battleships are placed
    Returns:
        list: _description_
    """
    
    for x in range(0, len(ships)): #loops through all ships in dictionary
        key = list(ships.keys())[x] #cast the ships key into a list
        value = list(ships.values())[x] #cast the ships values into a list
        
        #Deals with a simple placement
        if algorithm == "simple":
            for i in range(0, int(value)):
                board[x][i] = [key]
                
        #Block of code below deals with if we want a random placement
        elif algorithm == "random":
            invalid_placement = True
            while invalid_placement: #Keep looping if ships are overlapping
                invalid_placement = False
                start_row = random.randrange(0,9 - int(value)) 
                start_column = random.randrange(0,9 - int(value))
                #pick a random start point from the ship that wont overrun outside of the bounds 
                #based on the ships size
                rotation_integer = random.randrange(0,2)
                if rotation_integer == 0:
                    rotation = "h"
                else:
                    rotation = "v"
                #randomise rotation
                
                if rotation == "v":
                    for i in range(0, int(value)):
                        if board[start_row + i][start_column] != None:
                            invalid_placement = True
                #If vertical placement, check all vertical spots to make sure no ships overlap, if they do we loop again
                
                elif rotation == 'h':
                    for j in range(0, int(value)):
                        if board[start_row][start_column + j] != None:
                            invalid_placement = True
                #If horizontal placement, check all horizontal psots to make sure no ships overlap, if they do we loop again
            if rotation == "v":
                for i in range(0, int(value)):
                    board[start_row + i][start_column] = [key] #only loop through the row to place vertically
            elif rotation == 'h':
                for j in range(0, int(value)):
                    board[start_row][start_column + j] = [key] #only loop through the column to place horizontally
                    
        #Below deals with a custom placement from a json file
        elif algorithm == "custom":
            with open(ROUTE_FILE + 'placement.json') as ship_data:
                data = json.load(ship_data) #convert the json into a useable foramt
                json_values = list(data.values()) #make a list of the json values
            start_row = int(json_values[x][1]) #access the string stored in start x coord of json file for each ship and cast to int
            start_column = int(json_values[x][0])
            rotation = str(json_values[x][2]) #access the rotation from the json file for each ship and cast to string
            if rotation == 'v':
                for i in range(0, int(value)):
                    board[start_row + i][start_column] = [key] #only loop through the row to place vertically
            elif rotation == 'h':
                for j in range(0, int(value)):
                    board[start_row][start_column + j] = [key] #only loop through the column to place horizontally
                
    return board


#board = initialise_board()
#ships = create_battleships()
#place_battleships(board, ships, "random")
#
#for x in board:
#    print(x)
