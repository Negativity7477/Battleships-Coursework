import time
from components import place_battleships, initialise_board, create_battleships
import json

def attack(coordinates: tuple, board: list, battleships: dict) -> bool:
    """Takes in user defined coordinates and attacks that square

    Args:
        coordinates (tuple): attack coordinates given from user
        board (list): The representation of the board
        battleships (dict): The dictionary containing size and name of ships

    Returns:
        bool: returns whether that coordinate had a ship 
    """
    x_coord = coordinates[0]
    y_coord = coordinates[1]
    square_contents = board[x_coord][y_coord] 
    #sets square_content to whatever is in the square attacked by the user
    if square_contents == None: #If didn't hit a battleship
        is_hit = False
        print("You missed")
    else:
        is_hit = True
        board[x_coord][y_coord] = None 
        #square_contents is a string, so it must be converted to an int to decrement
        battleships[square_contents[0]] = str(int(battleships[square_contents[0]]) - 1)   
        print("You hit")   
        print(battleships)       
    return is_hit


def cli_coordinates_input() -> tuple:
    """Allows the user to input a coordinate

    Returns:
        tuple: The input coordinate
    """
    valid_coords = False
    while not valid_coords: #loop through while coords are bad
        coords = input("Enter a coord in the format x,y")
        try:
            coords = coords.split(",") #split up the x and y
            x_coord = int(coords[0])
            y_coord = int(coords[1])
            valid_coords = True #if there is no error, break the loop
        except TypeError: 
            valid_coords = False #keep looping until valid results
            raise TypeError("Please only use integers")
        except IndexError:
            valid_coords = False #keep looping until valid results
            raise IndexError("Please input inside of board")

        
    coordinates = (x_coord, y_coord)
    return coordinates
    

def simple_game_loop():
    """Loops through until the game is over
    """
    print("welcome to battleships")
    time.sleep(2.5) #Pauses on run
    battleships = create_battleships()
    board = initialise_board()
    place_battleships(board, battleships)
    game_over = False
    while not game_over: #loop through until all ships sunk
        coords = cli_coordinates_input()
        hit = attack(coords, board, battleships)
        if hit: #When we hit, update the board
            board[coords[0]][coords[1]] = None
        game_over = True
        for value in battleships.values():
            if value != '0': #Only run when all dict values are 0
                game_over = False       
    print("Game over")

if __name__ == '__main__':
    simple_game_loop()
