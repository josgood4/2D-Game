from Square import *
from Area import *
from Player import *
import pygame
import sys
#
# THIS GUIClass2.py works with PyGame in Python 2.7
#
#####################################################################
# TODO: implement action (GRASS) Square's - lambda expressions
#           ->events: "battle", "cut scene", "item pickup"
#             ("locked" doors check inventory and
#                    ifKey() => setWall(False), setMessage(""), changeSquare
#       Player inventory
#       make better instructions for the spreadsheet/an actual template
#       multi-Area support 
#       save state
#####################################################################

#Note: BLOCK_SIZE resides in Square.py
WIN_WIDTH = BLOCK_SIZE*9
WIN_HEIGHT = BLOCK_SIZE*8
BACKGROUND_COLOR = (0,0,0)

AREA_FILE = "areas/AreaTest.csv"

PLR_IMAGES = ["images/playerN.gif", "images/playerS.gif", \
              "images/playerE.gif", "images/playerW.gif"]

# These are the images for the Squares
#   EVERY image must be placed in the images folder,
#   (so it's accessed via "images/...")
#   the images should preferably be gifs (especially if transparency is needed
#   EVERY image name MUST start with "floo", "door", "wall", "inte", "acti"
IMAGES = ["images/floor_dirt.gif", "images/wall_rock.gif", \
        "images/door_ladder_down.gif", "images/door_ladder_up.gif", \
        "images/interactive_sign.gif", "images/interactive_door.gif", \
        "images/door_door.gif", "images/floor_door_mat.gif", \
        "images/wall_black.gif", "images/door_black.gif", \
        "images/wall_table_S.gif", "images/wall_table_N.gif", \
        "images/floor_indoors.gif", "images/floor_door_mat.gif" \
        ]

MESSAGE_BOX_IMG = "images/message_box.gif"

CONTROLS = {pygame.K_w: Player.N, pygame.K_s: Player.S, \
            pygame.K_a: Player.W, pygame.K_d: Player.E}

FONT = 'Fonts/Pokemon GB.ttf'
FONT_SIZE = 20
LINE_LIM = 21

######################################################

class GUIClass():
  
  def __init__(self):

    # setup Pygame and Font stuff:
    pygame.init()
    pygame.font.init()
    self.__myFont = pygame.font.Font(FONT, FONT_SIZE)
    self.__screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    self.__txtBox = pygame.image.load(MESSAGE_BOX_IMG)

    # INIT Square, Player, Area (in that order)
    Square.INIT(self.__screen, IMAGES)
    Player.INIT(self.__screen, PLR_IMAGES)
    Area.INIT(self.__screen, IMAGES)

    # Then make instances of Player and Area (in that order)
    self.__me = Player()
    self.__myA = Area(AREA_FILE, self.__me)
    #self.__myA.processData(areaInfo[0])
    #self.__myA.initTest()

    ######################################################
    #             ACTUAL GAME LOGIC BELOW                #
    ######################################################

    self.__update()

    eve = False  #short for eve, not to be confused with the event used below vvv

    while True:
      for event in pygame.event.get():
        # how to quit loop
        if event.type == pygame.QUIT:
          #can make this a separate function if desired
          pygame.display.quit()
          pygame.quit()
          sys.exit()
          
        if event.type == pygame.KEYDOWN:

          # for moving the player:
          if event.key in CONTROLS:
            self.__movePlayer(CONTROLS[event.key])

          # for interacting with signs, etc:
          if event.key == pygame.K_e:
            if self.__myA.getSquare(self.__me.getFacedPos()).getMessage():
              self.__txtBoxLogic()
              
            elif eve:
              ##print eve
              self.__update()
              eve = False
              ##messagebox.showinfo("Event", \
                      ##self.__myA.getSquare(self.__me.getFacedPos()).getMessage())

      pygame.display.update()

  ######################################################
    
  def __movePlayer(self, direction):
    self.__me.setFacing(direction)
    self.__me.move(self.__me.getRelFacedPos())
    if self.__myA.getSquare(self.__me.getCurPos()).isWall():
      self.__me.move(self.__me.getInvRelPos())
    elif self.__myA.getSquare(self.__me.getCurPos()).isDoor():
      self.__me.setCurPos(self.__myA.getSquare(self.__me.getCurPos()).getLoc2())
    self.__update()
        
  # If using __oldUpdate, switch Player.drawMe() method to alternative method
  # __oldUpdate() has a static background with moving player
  def __oldUpdate(self):
    for i in range(20):
      for j in range(10):
        self.__myA.getSquare((i,j)).drawMe((i,j))

    self.__me.drawMe(self.__me.getCurPos())

  # __update() moves the background while keeping the player stationary
  def __update(self):
    self.__myA.drawArea()    
    self.__me.drawMe()  # necessary for changes in direction

  ######################################################

  def __txtBoxLogic(self):
    lines = self.__getMessage()
    # display first 2 (or 1) lines
    self.__dispMessage(lines, 0)
    i = 2
    # if there are more lines to display, display them
    while len(lines) > i:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
          self.__dispMessage(lines, i)
          i += 2
    # have user hit <e> again to get rid of txtBox
    done = False
    while not(done):
      for event in pygame.event.get():
        done = True if(event.type == pygame.KEYDOWN and event.key == pygame.K_e) else False
    self.__update()

  def __dispMessage(self, lines, idx):
    # display txtBox
    self.__screen.blit(self.__txtBox, Square.getScaledLoc((6, 0)))
    
    # display top line
    txtImg = self.__myFont.render(lines[idx], False, (0,0,0))
    self.__screen.blit(txtImg, Square.getScaledLoc((6.5, 0.33)))
    
    # if there's a second line to display, display it
    if len(lines) > idx+1:
      txtImg2 = self.__myFont.render(lines[idx+1], False, (0,0,0))
      self.__screen.blit(txtImg2, Square.getScaledLoc((7.25, 0.33)))
      
    pygame.display.update()
    

  # __getMessage breaks up the message by lines, based on LINE_LIM, defined above
  #   and returns a list, lines, of those broken-up lines
  def __getMessage(self):
    txt = self.__myA.getSquare(self.__me.getFacedPos()).getMessage()
    ##print txt
    wrds = txt.split()
    i = 0
    start = i
    lengths = 0
    lines = []
    while i < len(wrds):
      lengths += len(wrds[i]) + 1
      if lengths/LINE_LIM >= len(lines)+1 or (lengths-1)/LINE_LIM >= len(lines)+1:
        lines.append(" ".join(wrds[start:i]))
        start = i
      i += 1
    lines.append(" ".join(wrds[start:]))
    return lines


GUIClass()
