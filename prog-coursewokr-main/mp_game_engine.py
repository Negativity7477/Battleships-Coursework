import components
import game_engine
import random
import time

players = {}

def initialise_player(username:str, algorithm:list = ["custom", "placement.json"]) -> dict:
    """Initialises the dictionary 'players and globalises it

    Args:
        player (str): this allows the function be called with either 2 players, or a player and AI
        algorithm (str): this allows the function to choose how to place battleships 
    Returns:
        dict: the players dictionary where key is a username and value is a list of board and battleship
    """
    board = components.initialise_board() 
    battleships = components.create_battleships() 
    board = components.place_battleships(board = board, ships = battleships, algorithm_and_filename = algorithm)
    
    players[username] = {'board':board, 'ships':battleships} #Create the dictionary, key as username, values are board and battleships
    return players


def generate_attack(player_board:list) -> tuple:
    """Generates an AI attack at coordinates yet to be hit
    Args:
        board (list): the players board to attack
    Returns:
        tuple: coordinates to attack the player board
    """
    #Loop through coordinates untill the AI hits new coordinates 
    old_coordinates = True
    while old_coordinates:
        old_coordinates = False
        random_x = random.randrange(0, len(player_board)) 
        random_y = random.randrange(0,len(player_board))  
        #creates a set of random coordinates within board
        if player_board[random_x][random_y] == "X" or player_board[random_x][random_y] == "O": #Checks if we have hit this coordinate before
            old_coordinates = True #only breaks if it is a new square
    coordinates = (random_x, random_y)
    return coordinates
    
    
def print_board(board:list):
    """Prints an ascii representation of the board
    Args:
        board: the board to represent
    """     
    ascii_rep = components.initialise_board(len(board)) #Create a new board to print
    #Loop through both grids (same size) and based on the main board we recieve, we add it to ascii_rep
    #Meaning we can print an ascii representation of the main board
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
    username_1 = input("enter username 1") #Take the username for player
    username_2 = "AI" #This is the AI loop, so username_2 will be AI
    
    algorithm = game_engine.find_algorithm()
    algorithm_and_filename = [algorithm,"placement.json"]
    player_1_dict = initialise_player(username_1, algorithm_and_filename)
    ai_dict = initialise_player(username_2, algorithm= "simple")

    global player_board #player_board is used in other functions so must be globalised
    player_board = player_1_dict[username_1]['board']
    player_ships = player_1_dict[username_1]['ships']
    ai_board = ai_dict[username_2]['board']
    ai_ships = ai_dict[username_2]['ships']
    #extract the player's and AI's boards and ships into variables to use
    
    finished = False #flag to loop 
    while not finished:
        old_coords = True #Loops while attacking previously attack coords
        while old_coords:
            attack_coords = (-1, -1)
            while attack_coords == (-1, -1):
                attack_coords = game_engine.cli_coordinates_input() #Generate attack coordinates
            try:
                if ai_board[attack_coords[0]][attack_coords[1]] == "X" or ai_board[attack_coords[0]][attack_coords[1]] == "O":
                    old_coords = True
                    print("Please attack new coordinates")
                else:
                    old_coords = False #Break the loop
            except IndexError:
                print("please input a value within the board")
                continue
        print("Player, ")#Allows the ability to distinguish between players and AI attacks
        game_engine.attack(attack_coords, ai_board, ai_ships)

        print("Ai, ") #Allows the ability to distinguish between players and AI attacks
        ai_attack = generate_attack(player_board)
        game_engine.attack(ai_attack, player_board, player_ships)
        print_board(player_board)

        no_ai_ships = all(value == '0' for value in ai_ships.values())  
        no_player_ships = all(value == '0' for value in player_ships.values())
        #Check all ship sizes in the both dictionaries.
        
        if no_ai_ships: #All ai ships have been sunk
            print("Congratulations! You have won.")
            finished = True
        elif no_player_ships: #All player ships haveb een sunk
            print("Unfortunately, you have lost.")
            finished = True
    
def multiplayer_game_loop():
    """This function allows 2 people to play against each other in the command line
    """
    
    
    print("welcome to battleships")
    time.sleep(2.5) #Pauses on run
    username_1 = input("enter username 1") #Take the username for player
    username_2 = input("enter username 2") #Take the second username
    
    
    algorithm_1 = game_engine.find_algorithm()
    algorithm_2 = game_engine.find_algorithm()
    algorithm_and_filename = [algorithm_1, "placement.json"] #In order to allow either files to be used, we create a list
    algorithm_and_filename_2 = [algorithm_2, "2_player_placement.json"]
    player_1_dict = initialise_player(username_1, algorithm_and_filename)
    player_2_dict = initialise_player(username_2, algorithm_and_filename_2)

    global player_board_1 #player_board is used in other functions so must be globalised
    player_board_1 = player_1_dict[username_1]['board']
    player_ships_1 = player_1_dict[username_1]['ships']
    global player_board_2 #We will also need to use player_board_2 
    player_board_2 = player_2_dict[username_2]['board']
    player_ships_2 = player_2_dict[username_2]['ships']
    #extract the player's boards and ships into variables to use
    
    finished = False #flag to loop 
    while not finished:
        old_coords = True #Loops while attacking previously attack coords
        while old_coords:
            attack_coords = (-1,-1)
            while attack_coords == (-1,-1):
                attack_coords = game_engine.cli_coordinates_input() #Generate attack coordinates
            try:
                if player_board_2[attack_coords[0]][attack_coords[1]] == "X" or player_board_2[attack_coords[0]][attack_coords[1]] == "O":
                    old_coords = True
                    print("Please attack new coordinates")
                else:
                    old_coords = False #Break the loop
            except IndexError:
                print("please input a value within the board")
                continue
            
            print("Player 1, ")#Player 1's turn
            game_engine.attack(attack_coords, player_board_2, player_ships_2)
            print("Player 2, ")#Player 2's turn
        
        while True:
            attack_coords = (-1,-1)
            while attack_coords == (-1,-1):
                attack_coords = game_engine.cli_coordinates_input()
            hit = game_engine.attack(attack_coords, player_board_1, player_ships_1)
            if hit == None:
                print("please input a value within the board")
                continue
            else:
                break
        
        no_player_ships_1 = all(value == '0' for value in player_ships_1.values())
        no_player_ships_2 = all(value == '0' for value in player_ships_2.values())  
        #Check all ship sizes in the both dictionaries.
        
        if no_player_ships_1: #All player 2's ships have been sunk
            print_board(player_board_1)
            print("---------------------") #Print both player's boards to show where their ships were
            print_board(player_board_2)
            print(f"Congratulations! You have won {username_1}.")
            finished = True 
        elif no_player_ships_2: #All player 1's ships have been sunk
            print_board(player_board_1)
            print("---------------------") #Print both player's boards to show where their ships were
            print_board(player_board_2)
            print(f"Congratulations! You have won {username_2}.")
            finished = True



if __name__ == "__main__":
    opponent = ""
    while opponent != "1" and opponent != "2":
        opponent = input("Press 1 for AI opponent, press 2 to play against another person")
    if opponent == "1":
        ai_opponent_game_loop()
    else:
        multiplayer_game_loop()