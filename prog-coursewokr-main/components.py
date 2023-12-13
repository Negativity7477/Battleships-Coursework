import json
import random


def initialise_board(size: int = 10) -> list:
    """Creates an empty board of a given size
    Args:
        size (int, optional): Size of the grid to play on. Defaults to 10.
    Returns:
        list: Return a list of list of containing NONE values
    """
    board_list = [[None for x in range(0, size)] for y in range(0, size)]
    # Produces a grid of x rows and x columns
    return board_list


def create_battleships(filename: str = "battleships.txt") -> dict:
    """Creates the battleships as a dictionary that can then later be placed
    Args:
        filename (str, optional): A file containing the battleships names and size.
        Defaults to "battleships.txt".
    Returns:
        dict: Dictionary with the name of the ships as keys and the size of the ships as the values
    """

    battleships = {}
    with open(filename) as text_file:
        for line in text_file:
            line = line.strip()
            (key, val) = line.split(":")  # Split the key and value up from the colon
            battleships[key] = int(val)  # Add the integer value to the dictionary

    return battleships


def place_battleships(
    board: list, ships: dict, algorithm: list = ["custom", "placement.json"]) -> list:
    """A function to place down the ships
    we can choose what method to place down the ships and if we want to use custom placement,
    we can choose 1 or 2 json files to use.
    Args:
        board (list): Empty list of list from initialise_board
        ships (dict): Dictionary of ships from create_battleships
        algorithm (str): Allows the user to select how the battleships are placed
        and which file custom should place
    Returns:
        list: returns the board with the battleships placed as required
    """

    place_type = algorithm[0]  # Unpack the algorithm to place
    filename = algorithm[1]  # Unpack the filename to use to place

    for x in range(0, len(ships)):  # loops through all ships in dictionary
        key = list(ships.keys())[x]  # cast the ships key into a list
        value = list(ships.values())[x]  # cast the ships values into a list

        # Deals with a simple placement
        if place_type == "simple":
            for i in range(0, int(value)):
                board[x][i] = [key]

        # Block of code below deals with if we want a random placement
        elif place_type == "random":
            invalid_placement = True
            while invalid_placement:  # Keep looping if ships are overlapping
                invalid_placement = False
                start_row = random.randrange(0, 9 - int(value))
                start_column = random.randrange(0, 9 - int(value))
                # pick a random start point from the ship that wont overrun outside of the bounds
                # based on the ships size
                rotation_integer = random.randrange(0, 2)
                if rotation_integer == 0:
                    rotation = "h"
                else:
                    rotation = "v"
                # randomize rotation

                if rotation == "v":
                    for i in range(0, int(value)):
                        if board[start_row + i][start_column] is not None:
                            invalid_placement = True
                # If vertical placement, check all vertical spots to make sure no ships overlap,
                # if they do we loop again

                elif rotation == "h":
                    for j in range(0, int(value)):
                        if board[start_row][start_column + j] is not None:
                            invalid_placement = True
                # If horizontal placement, check all horizontal spots to make sure no ships overlap,
                # if they do we loop again
            if rotation == "v":
                for i in range(0, int(value)):
                    board[start_row + i][start_column] = [
                        key
                    ]  # only loop through the row to place vertically
            elif rotation == "h":
                for j in range(0, int(value)):
                    board[start_row][start_column + j] = [
                        key
                    ]  # only loop through the column to place horizontally

        # Below deals with a custom placement from a json file
        elif place_type == "custom":
            try:
                with open(filename) as ship_data:
                    data = json.load(ship_data)  # convert the json into a usable format
                    json_values = list(data.values())  # make a list of the json values
                start_row = int(json_values[x][1])
                # get the string stored in start x coord of json file for each ship and cast to int
                start_column = int(json_values[x][0])
                # get the string stored in start y coord of json file for each ship and cast to int
                rotation = str(json_values[x][2])
                # get the rotation from the json file for each ship and cast to string
                if rotation == "v":
                    for i in range(0, int(value)):
                        board[start_row + i][start_column] = [key]
                        # only loop through the row to place vertically
                elif rotation == "h":
                    for j in range(0, int(value)):
                        board[start_row][start_column + j] = [key]
                        # only loop through the column to place horizontally
            except ValueError:
                print(
                    "The program will now close, please make sure to use integer"+
                    "values in placement.json in order for the program to run"
                )
                exit()
            except IndexError:
                print(
                    "The program will now close"+
                    "keep the values inside the bounds of the board in order for the program to run"
                )
                exit()

    return board
