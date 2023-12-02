import time
import components
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
    return is_hit


def cli_coordinates_input() -> tuple:
    """Allows the user to input a coordinate

    Returns:
        tuple: The input coordinate
    """
    while True: #loop through while coords are bad
        try:
            coords = input("Enter a coord in the format x,y")
            x_coord, y_coord = map(int, coords.split(',')) #split up the x and y and cast to int
            coordinates = (x_coord, y_coord)
            return coordinates #break the loop and return if hasn't crashed 
        except ValueError: 
            print("Please only use integers")
        except IndexError:
            print("Please input inside of board")

        
    

def simple_game_loop():
    """Loops through until the game is over
    """
    print("welcome to battleships")
    time.sleep(2.5) #Pauses on run
    battleships = components.create_battleships()
    board = components.initialise_board()
    components.place_battleships(board, battleships, "custom")
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
