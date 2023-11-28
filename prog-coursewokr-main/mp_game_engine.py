import components
import game_engine
import random
import time

players = {}

def initialise_players() -> dict:
    username_1 = input("Enter username one")
    username_2 = input("Enter username two")
    
    board = components.initialise_board()
    
    battleships_1 = components.create_battleships()
    board_1 = components.place_battleships(board=board, ships = battleships_1)
    battleships_2 = components.create_battleships()
    board_2 = components.place_battleships(board=board, ships = battleships_2)
    
    return players

def generate_attack() -> tuple:
    """generates an AI attack

    Returns:
        tuple: coordinates to attack the player board
    """
    random_x = random.randrange(0, len(board))
    random_y = random.randrange(0,len(board))
    coordinates = (random_x, random_y)
    return coordinates
    
    
def ai_opponent_game_loop():
    print("welcome to battleships")
    time.sleep(2.5) #Pauses on run
    players = initialise_players()
    