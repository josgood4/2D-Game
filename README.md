# 2D-Game
A framework for the implementation of a Pokemon-style two-dimensional game

## Prerequisites:
- Python 2.7.12
- Pygame 1.9

## Creating an Area: An Overview
1) Download [this template](https://docs.google.com/spreadsheets/d/1N7aVqXMlO4WnsL-LR1LV_OpQzQNBnMpR2YgeEsVCMSQ/edit?usp=sharing)
2) Create shortcuts for your graphics on Sheet 2
3) Create whatever pattern of graphics you'd like on Sheet 1
4) Add any special instructions to Row 1 of Sheet 3
5) Export Sheet 3 as a .csv file
6) In GUIClass2.py, set the value of AREA_FILE to the file name of your .csv file
7) Run GUIClass2.py!

## Creating an Area: More Details
### Names of Graphics 
Be careful how you name your graphics files, as the first 4 characters of your graphic files' names identify what kind of tile they are:
  * "floo" - a "floor" tile - can be walked on freely
  * "wall" - a "wall" tile - cannot be walked into
  * "door" - a "door" tile - teleports the player to another tile
  * "acti" - an "action" tile - actions happen on these tiles (NOT YET IMPLEMENTED)
  * "inte" - an "interactive" tile - the player can walk up to these tiles and hit "E" to interact with them
  
### Pattern stipulations
Okay, you can't just make ANY pattern you want - be sure to:
  * Enclose every Area with walls (so the player can't walk on an unloaded Square)
  * Have at least 4 "wall" squares as padding on the bottom and right side of your area. This way, the player can't even walk near a tile that isn't loaded.
  
    (Don't worry about the top and left sides - Python's negative indexing accesses items from the end of lists, so when it needs to render the "-1st" row, it'll just render the bottom row) 
    
### Special Instructions
Special instructions make squares do more than act as just "walls" or "floors".
    They are each of the form: `COMD arg1 arg2 arg3 ...` with at least 3 arguments
  * Player Init: `PLRI <initial_row> <initial_col> <initial_facing>`
    * `<initial_row>` and `<initial_col>` are the starting position of the player (rows and col's are zero-indexed)
    * `<initial_facing>` is the initial direction the player is facing - according to the key on Sheet 2
    * If you do not provide this instruction, the player will default to starting on square (1,1) and facing South
  * Lock: `LOCK <row> <col> <0_or_1>`
    * `<row>` and `<col>` are the row and col of the "door" to be locked
    * `<0_or_1>` represents whether the door begins locked - 0 for False, 1 for True
  * Message: `MESS <row> <col> <message>`
    * I think you get the idea now with `<row>` and `<col>`
    * `<message>` is a message to display when the player interacts with the given square
  * Location 2: `LOC2 <row> <col> <row2>, <col2>`
    * Again, same deal with `<row>` and `<col>`
    * `<row2>` and `<col2>` represent the coordinates where the player will be teleported if he/she steps on the square at `<row>, <col>`
    
 ### Controls
 To move the player, use the WASD keys. You can also interact with some objects using the E key
  
