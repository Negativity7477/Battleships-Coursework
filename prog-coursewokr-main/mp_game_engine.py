import components
import game_engine
import random
import time

players = {}

def initialise_player(username:str, algorithm:str = "custom") -> dict:
    """Initialises the dictionary 'players and globalises it

    Args:
        player (str): this allows the function be called with either 2 players, or a player and AI
        algorithm (str): this allows the function to choose how to place battleships 
    Returns:
        dict: the players dictionary where key is a username and value is a list of board and battleship
    """
    
    board = components.initialise_board() 
    battleships = components.create_battleships() 
    board = components.place_battleships(board=board, ships = battleships, algorithm= algorithm)
    
    global players
    players[username] = {'board':board, 'ships':battleships} #key is username and board together (i think)
    return players

def generate_attack(player_board:list) -> tuple:
    """generates an AI attack at unhit coordinates
    Args:
        board (list): the players board to attack
    Returns:
        tuple: coordinates to attack the player board
    """
    old_coordinates = True
    while old_coordinates:
        old_coordinates = False
        random_x = random.randrange(0, len(player_board)) 
        random_y = random.randrange(0,len(player_board))  #creates a set of random coordinates within board
        if player_board[random_x][random_y] == "X" or player_board[random_x][random_y] == "O": #Checks if we have hit this coordinate before
            old_coordinates = True #only breaks if it is a new square
    coordinates = (random_x, random_y)
    return coordinates
    
    
def print_board(board:list):
    """Prints an ascii representation of the board
    Args:
        board: the board to represent
    """     
    ascii_rep = components.initialise_board(len(board))
    for rows in range(0, len(board)):
        for columns in range(0, len(board)):
            if board[rows][columns] == None:
                ascii_rep[rows][columns] = "."
            elif board[rows][columns] == "X":
                ascii_rep[rows][columns] = "X"
            elif board[rows][columns] == "O":
                ascii_rep[rows][columns] = "O"
            else:
                ascii_rep[rows][columns] = "="
    for x in ascii_rep:
        print(x)

    
def ai_opponent_game_loop():
    """The main loop that runs if this is the main file. This allows the player to 
    go against an AI opponent
    """
    print("welcome to battleships")
    time.sleep(2.5) #Pauses on run
    username_1 = input("enter username 1")
    username_2 = "AI"
    player_1_dict = initialise_player(username_1)
    ai_dict = initialise_player(username_2, algorithm= "simple")

    global player_board
    player_board = player_1_dict[username_1]['board']
    player_ships = player_1_dict[username_1]['ships']
    ai_board = ai_dict[username_2]['board']
    ai_ships = ai_dict[username_2]['ships']
    #extract the player's and AI's boards and ships into variables to use

    finished = False #flag to loop through
    while not finished:
        old_coords = True #Loops while attacking previously attack coords
        while old_coords:
            attack_coords = game_engine.cli_coordinates_input()
            if ai_board[attack_coords[0]][attack_coords[1]] == "X" or ai_board[attack_coords[0]][attack_coords[1]] == "O":
                old_coords = True
                print("Please attack new coordinates")
            else:
                old_coords = False
        
        print("Player, ")#Allows the ability to distinguish between players and AI attacks
        game_engine.attack(attack_coords, ai_board, ai_ships)

        print("Ai, ") #Allows the ability to distinguish between players and AI attacks
        ai_attack = generate_attack(player_board)

        game_engine.attack(ai_attack, player_board, player_ships)

        print_board(player_board)

        no_ai_ships = all(value == '0' for value in ai_ships.values())  
        no_player_ships = all(value == '0' for value in player_ships.values())
        #Check all ship sizes in the both dictionaries.
        print(no_ai_ships)
        
        if no_ai_ships: #All ai ships have been sunk
            print("Congratulations! You have won.")
            finished = True
        elif no_player_ships: #All player ships haveb een sunk
            print("Unfortunately, you have lost.")
            finished = True
    

if __name__ == "__main__":
    ai_opponent_game_loop()