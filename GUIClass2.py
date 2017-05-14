from Square import *
from Area import *
from Player import *
import pygame
import csv
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
LINE_LIM = 28

AREA_FILE = "areas/AreaTest.csv"

IMG_DIR = "images/"

PLR_IMAGES = ["playerN.gif", "playerS.gif", "playerE.gif", "playerW.gif"]
for i in range(len(PLR_IMAGES)):
  PLR_IMAGES[i] = IMG_DIR + PLR_IMAGES[i]

# EVERY image must be placed in the images folder,
#   (so it's accessed via "images/...")
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

FONT = 'PT Serif'
FONT_SIZE = 40

######################################################

class GUIClass():
  
  def __init__(self):
    self.__PLR_INIT_POS = [1,1]
    self.__PLR_INIT_FACE = Player.S
    
    pygame.init()
    pygame.font.init()
    self.__myFont = pygame.font.SysFont(FONT, FONT_SIZE) #<-FIX ME
    self.__screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    self.__txtBox = pygame.image.load(MESSAGE_BOX_IMG)
    #self.__screen.fill(BACKGROUND_COLOR)

    Square.INIT(self.__screen, IMAGES)
    self.__me = Player(self.__screen, self.__PLR_INIT_POS, self.__PLR_INIT_FACE, PLR_IMAGES)
    Area.INIT(self.__screen, self.__me, IMAGES)
    
    self.__myA = Area(self.__loadArea())
    #self.__myA.processData(areaInfo[0])
    #self.__myA.initTest()

    ######################################################

    self.__update()

    eve = False  #short for eve, not to be confused with the event used below vvv
    firstLine = True

    while True:
      for event in pygame.event.get():
        # how to quit loop
        if event.type == pygame.QUIT:
          #can make this a separate function if desired
          pygame.display.quit()
          pygame.quit()
          sys.exit()
          
        if event.type == pygame.KEYDOWN:
          
          if event.key in CONTROLS:
            self.__movePlayer(CONTROLS[event.key])
            
          if event.key == pygame.K_e:
            ##print '<A>'
            if self.__myA.getSquare(self.__me.getFacedPos()).getMessage() and not(eve):
              lines = self.__getMessage()
              ##print lines
              
              ##print initial line:
              if firstLine:
                txtImg = self.__myFont.render(lines[0], True, (0,0,0))
                self.__screen.blit(txtImg, Square.getScaledLoc((6.33, 0.33)))
                ##print txt[0:LINE_LIM]
                #CONDESE THIS:
                if len(lines) > 1:
                  txtImg2 = self.__myFont.render(lines[1], True, (0,0,0))
                  self.__screen.blit(txtImg2, Square.getScaledLoc((7.00, 0.33)))
                  ##print txt[LINE_LIM:LINE_LIM*2]
                i=2
                if len(lines) > 2:
                  firstLine = False
                else:
                  eve = True
                
              #print remaining lines:
              elif not(firstLine):
                txtImg = self.__myFont.render(lines[i], True, (0,0,0))
                self.__screen.blit(txtImg, Square.getScaledLoc((6.33, 0.33)))
                if len(lines) > i+1:
                  txtImg2 = self.__myFont.render(lines[i+1], True, (0,0,0))
                  self.__screen.blit(txtImg2, Square.getScaledLoc((7.00, 0.33)))
                ##print str(len(lines)) + " " + str(i)
                i += 2
                if len(lines) <= i:
                  firstLine = True
                  eve = True
              ##print eve
              
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
    if self.__myA.getSquare(self.__me.getCurPos()).isDoor():
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

  def __loadArea(self):
    f = open(AREA_FILE)
    reader = csv.reader(f)
    
    rows = []
    for line in reader:
      rows.append(line)

    f.close()
    return rows

  ######################################################

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
    self.__screen.blit(self.__txtBox, Square.getScaledLoc((6, 0)))
    return lines


GUIClass()
