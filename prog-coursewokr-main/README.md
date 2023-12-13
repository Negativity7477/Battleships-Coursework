 # Battleships-Coursework

This program runs the game battleships. It can run with a web interface by running main and going to local host, or it can run in the terminal by running mp_game_engine. This was built as a piece of University coursework.

  
Prerequisites -

- Python 3.9.13

- Flask

- Pytest

- Inspect

- Importlib

- tests.tests_helper_functions

- Random


Getting started tutorial (if program does not run because of a file error, look at developer documentation section) -

1. Playing in command line against a random AI board using a random or simple placement where simple is all the ships horizontal in the top left corner - 
- Run the module mp_game_engine.py 
- Input "1" when prompted in terminal (no space)
- Enter a username
- Input "simple" or "random"  (not case sensitive)
- The game will run, simply input coordinates to attack when prompted to attack a randomly generated AI board.

2. Playing in command line against a random AI board using a custom placed board - 
- Open the file "placement.json"
- Change the json file to have the coordinates and rotation of the ships you want (Note the format is [start x coordinate, start y coordinate, rotation])
- Make sure these values are valid (integers within the bounds of the board) otherwise the program will flag an error
- Play the game as before, but instead of inputting simple or random when prompted, input custom

3. Multiplayer in command line -
- Run the module mp_game_engine.py 
- Input "2" when prompted in terminal 
- Enter a username for player 1
- Enter a username for player 2
- Choose player 1's ship placement type
- Custom runs off "placement.json" for player 1, change this file as mentioned before to change where the ships should be
- Choose player 2's ship placement 
- Custom runs off "2_player_placement.json" for player 2, this file is exactly the same as "placement.json" but will allow both players to use a custom placement, this file should be changed for wherever player 2's wants their ships
- Play the game as above 

3. Playing using the web interface against an AI using a random board - 
- Run the module "main.py"
- Open your browser and go to 127.0.0.1:5000/placement
- Here you can place all your ships down and rotate the ships if wanted 
- Once all 5 ships are placed, click send game to go to the main game
- Your board will be shown on the right, and you can attack any un hit coordinates on the board on the left. If the square lights up red, you hit a ship. If it lights up blue, you missed.
- Once the game ends, if you wish to replay, you must stop the server in terminal by pressing control + c, and rerunning main.py as before


Testing - 
In order to run the tests, make sure pytest is installed. In VSCode, open the testing section and configure tests. Use the pytests option and open in the root directory. 
We can then run the tests.
Note test_generate_attacK_return_type fails



Developer documentation -

Modules -  
The components module contains key functions for setting up the game. It does nothing for processing the game. It contains three functions, one for creating an empty board for use in other places, one for creating a dictionary containing the name of the battleships and their respective size and one to place those battle ships on the board in 3 different ways based on the arguments provided.  
The game_engine module contains a simple game loop to test the mechanics of the module. It has 3 other functions, one to process an attack, one to get the user input to attack a coordinate and one to allow the user to select which algorithm to place battleships with. Note that this last function can be run either to select which algorithm the user places the ships with or which function the AI places the ships with.
The mp_game_engine module allows for game play. There is a total of 5 functions. One initializes a dictionary with key of username and value board and ships. Another function allows for an ascii board to be printed. The last 3 functions are for game play. A function allows the AI to get coordinates to attack and the other 2 functions deal with AI and multiplayer opponents respectively. This module combines both game_engine and components in order to function
The main function incorporates the web interface to play. It contains 3 functions. One allows placement of ships on web interface, one renders the main game play board and the last allows attacking the board and updating the backend.


License - see LICENSE.txt, the project is licensed under the terms of the MIT license.
Details - {Contact details}
Authors - {Name}
