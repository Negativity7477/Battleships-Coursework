import components
import game_engine
import random
import time

players = {}

def initialise_players(player:str = "two") -> dict:
    """Initialises the dictionary players and globalises it

    Args:
        player (str): this allows the function be called with either 2 players, or a player and AI
    Returns:
        dict: the players dictionary where key is a username and value is a list of board and battleship
    """
    
    global username_1
    username_1 = input("Enter username one") #Globalise the username to use elsewhere
    board = components.initialise_board() 
    battleships_1 = components.create_battleships() 
    board_1 = components.place_battleships(board=board, ships = battleships_1, algorithm= "custom")
    dict_values_1 = [board_1, battleships_1]
    if player == "two": #Can have a second player or AI
        global username_2
        username_2 = input("Enter username two")
    else:
        username_2 = "AI"
    battleships_2 = components.create_battleships()
    board_2 = components.place_battleships(board=board, ships = battleships_2, algorithm="random")
    dict_values_2 = [board_2, battleships_2]
    #Create values for the other player, either AI or another person
    
    players = {username_1: dict_values_1, username_2:dict_values_2}
    
    
    player_ships = players[username_1][0]
    player_board = players[username_1][1]
    key, val = next(iter(players.items()))
    for x in val:
        print(x)
    
    for x in player_board:
        print(x)
    print("\n",player_ships)
    
    print(players)
    
    return players

def generate_attack(board:list) -> tuple:
    """generates an AI attack
    Args:
        board (list): the players board to attack
    Returns:
        tuple: coordinates to attack the player board
    """
    random_x = random.randrange(0, len(board)) 
    random_y = random.randrange(0,len(board))  #creates a set of random coordinates within board
    coordinates = (random_x, random_y)
    return coordinates
    
    
def print_board(board:list):
    """Prints an ascii representation of the board
    Args:
        board: the board to represent
    """    
    ascii_rep = initialise_players(len(board))
    for rows in board:
        print(rows)
        for columns in rows:
            print(columns)
            if columns == None:
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
    players = initialise_players("AI")
    ai_board = players["AI"][0]
    ai_ships = players["AI"][1]
    player_board = players[username_1][0] #Something is going wrong here but i have no fucking clue what
    player_ships = players[username_1][1]
    finished = False #flag to loop through
    while not finished:
        attack_coords = game_engine.cli_coordinates_input()
        
        print("Player, ")#Allows the ability to distinguish between players and AI attacks
        game_engine.attack(attack_coords, ai_board, ai_ships)

        print("Ai, ") #Allows the ability to distinguish between players and AI attacks
        ai_attack = generate_attack(player_board)

        game_engine.attack(ai_attack, player_board, player_ships)

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