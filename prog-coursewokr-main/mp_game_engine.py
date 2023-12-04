import components
import game_engine
import random
import time

players = {}

def initialise_player(username:str) -> dict:
    """Initialises the dictionary 'players and globalises it

    Args:
        player (str): this allows the function be called with either 2 players, or a player and AI
    Returns:
        dict: the players dictionary where key is a username and value is a list of board and battleship
    """
    
    board = components.initialise_board() 
    battleships = components.create_battleships() 
    board = components.place_battleships(board=board, ships = battleships, algorithm= "custom")
    
    global players
    players[username] = {'board':board, 'ships':battleships} #key is username and board together (i think)
    return players

def generate_attack() -> tuple:
    """generates an AI attack
    Args:
        board (list): the players board to attack
    Returns:
        tuple: coordinates to attack the player board
    """
    random_x = random.randrange(0, len(player_board)) 
    random_y = random.randrange(0,len(player_board))  #creates a set of random coordinates within board
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
    ai_dict = initialise_player(username_2)

    global player_board
    player_board = player_1_dict[username_1]['board']
    player_ships = player_1_dict[username_1]['ships']
    ai_board = ai_dict[username_2]['board']
    ai_ships = ai_dict[username_2]['ships']
    #extract the player's and AI's boards and ships into variables to use

    finished = False #flag to loop through
    while not finished:
        attack_coords = game_engine.cli_coordinates_input()
        
        print("Player, ")#Allows the ability to distinguish between players and AI attacks
        game_engine.attack(attack_coords, ai_board, ai_ships)

        print("Ai, ") #Allows the ability to distinguish between players and AI attacks
        ai_attack = generate_attack()

        game_engine.attack(ai_attack, player_board, player_ships)

        print_board(player_board)

        no_ai_ships = all(value == 0 for value in ai_ships)  
        no_player_ships = all(value == 0 for value in player_ships)
        #Check all ship sizes in the both dictionaries.
        
        if no_ai_ships: #All ai ships have been sunk
            print("Congratulations! You have won.")
            finished = True
        elif no_player_ships: #All player ships haveb een sunk
            print("Unfortunately, you have lost.")
            finished = True
    

if __name__ == "__main__":
    ai_opponent_game_loop()