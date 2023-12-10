import time
import components
import json

def attack(coordinates: tuple, board: list, battleships: dict) -> bool:
    """Takes in user / AI defined coordinates and attacks that square

    Args:
        coordinates (tuple): attack coordinates given from user
        board (list): The representation of the board
        battleships (dict): The dictionary containing size and name of ships

    Returns:
        bool: returns whether that coordinate had a ship 
    """
    x_coord = coordinates[0]
    y_coord = coordinates[1]
    try:
        square_contents = board[x_coord][y_coord] 
        #sets square_content to whatever is in the square attacked by whatever called the function
    except IndexError:
        return None #The only error that can occur here is an IndexError, so we return None if it is an error
    
    if square_contents == None: #If didn't hit a battleship
        is_hit = False
        board[x_coord][y_coord] = "O" #This is to show that this coord has been shot and missed for later use
        print("You missed")
    else:
        is_hit = True
        board[x_coord][y_coord] = None 
        #square_contents is a string, so it must be converted to an int to decrement
        battleships[square_contents[0]] = str(int(battleships[square_contents[0]]) - 1)   
        board[x_coord][y_coord] = "X" #After processing the attack, we show it has been shot for later use
        print("You hit")         
    return is_hit


def cli_coordinates_input() -> tuple:
    """Allows the user to input a coordinate

    Returns:
        tuple: The input coordinate
    """
    try:
        coords = input("Enter a coord in the format x,y")
        x_coord, y_coord = map(int, coords.split(',')) #split up the x and y and cast to int
        if x_coord > -1 and y_coord > -1:
            coordinates = (x_coord, y_coord)
        else:
            print("Positive integers only")
            coordinates = (-1, -1)
        #This if else block checks to make sure the values are positive
        
        return coordinates #break the loop and return if hasn't crashed 
    
    except ValueError: #Catch value exceptions when inputing non ints
        print("Please only use integers")
        coordinates = (-1, -1)
        
    except IndexError: #Catch index exceptions when out of board
        print("Please input inside of board")
        coordinates = (-1, -1)
        
    except: #Catch other exceptions
        print("An error occured, make sure your input is within the board and an integer")
        coordinates = (-1, -1)
        
    return coordinates

def find_algorithm() -> str:
    """This function allows the user to pick which algorithm to place
    ships with

    Returns:
        str: the algorithm to use
    """
    valid_algorithm = False
    while not valid_algorithm: 
        valid_algorithm = True
        algorithm = input("Please enter an algorithm to place your ships, simple, random or custom")
        algorithm = algorithm.lower()
        if algorithm != "simple" and algorithm != "random" and algorithm != "custom":
            valid_algorithm = False
            print("please use one of the 3 algorithms")
    return algorithm
    

def simple_game_loop():
    """Loops through until the game is over
    """
    print("welcome to battleships")
    time.sleep(2.5) #Pauses on run
    battleships = components.create_battleships()
    board = components.initialise_board()
    algorithm = find_algorithm()
    algorithm_and_filename = [algorithm, "placement.json"]
    components.place_battleships(board, battleships, algorithm_and_filename=algorithm_and_filename)
    game_over = False
    while not game_over: #loop through until all ships sunk
        coords = (-1, -1)
        while coords == (-1, -1):
            coords = cli_coordinates_input()
        hit = attack(coords, board, battleships)
        if hit == None:
            print("please input a value within the board")
            continue
        elif hit: #When we hit, update the board
            board[coords[0]][coords[1]] = None
        game_over = True
        for value in battleships.values():
            if value != '0': #Only run when all dict values are 0
                game_over = False      
    print("Game over")

if __name__ == '__main__':
    simple_game_loop()
