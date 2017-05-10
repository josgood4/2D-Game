from Square import *
from Area import *
from Player import *
import pygame
import csv
import sys
#
# THIS GUIClass2 works with PyGame in Python 2.7
#
#####################################################################
# TODO: implement action (GRASS) Square's - lambda expressions }->locked doors
#       make better instructions for the spreadsheet/an actual template
#       multi-Area support
#       hypens in text boxes
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

IMAGES = ["floor_dirt.gif", "wall_rock.gif", \
        "door_ladder_down.gif", "door_ladder_up.gif", \
        "interactive_sign.gif", "interactive_door.gif", \
        "door_door.gif", "floor_door_mat.gif", \
        "wall_black.gif", "door_black.gif", \
        "wall_table_S.gif", "wall_table_N.gif", \
        "floor_indoors.gif", "floor_door_mat.gif" \
        ]
for i in range(len(IMAGES)):
  IMAGES[i] = IMG_DIR + IMAGES[i]

class GUIClass():
  
  def __init__(self):
    self.__PLR_INIT_POS = [1,1]
    self.__PLR_INIT_FACE = Player.S
    
    pygame.init()
    pygame.font.init()
    self.__myFont = pygame.font.SysFont('PT Serif', 40) #<-FIX ME
    self.__screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    self.__txtBox = pygame.image.load("images/message_box.gif")
    #self.__screen.fill(BACKGROUND_COLOR)

    Square.INIT(self.__screen, IMAGES)
    self.__me = Player(self.__screen, self.__PLR_INIT_POS, self.__PLR_INIT_FACE, PLR_IMAGES)
    Area.INIT(self.__screen, self.__me)
    
    areaInfo = self.__loadArea()
    self.__myA = Area(areaInfo[1:])  #first row contains other data
    self.__processData(areaInfo[0])
    #self.__myA.initTest()

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
          if event.key == pygame.K_w:
            ##print 'up'
            self.__me.setFacing(Player.N)
            self.__me.move((-1,0))
            if self.__myA.getSquare(self.__me.getCurPos()).isWall():
              self.__me.move((1,0))
            self.__update()
               
          if event.key == pygame.K_s:
            ##print 'down'
            self.__me.setFacing(Player.S)
            self.__me.move((1,0))
            if self.__myA.getSquare(self.__me.getCurPos()).isWall():
              self.__me.move((-1,0))
            self.__update()
               
          if event.key == pygame.K_a:
            ##print 'left'
            self.__me.setFacing(Player.W)
            self.__me.move((0,-1))
            if self.__myA.getSquare(self.__me.getCurPos()).isWall():
              self.__me.move((0,1))
            self.__update()
            
          if event.key == pygame.K_d:
            ##print 'right'
            self.__me.setFacing(Player.E)
            self.__me.move((0,1))
            if self.__myA.getSquare(self.__me.getCurPos()).isWall():
              self.__me.move((0,-1))
            self.__update()

          if event.key == pygame.K_e:
            ##print '<A>'
            if self.__myA.getSquare(self.__me.getFacedPos()).getMessage() and not(eve):
              txt = self.__getMessage()
              ##print "'" + txt + "'"
              
              ##print initial line:
              if firstLine:
                txtImg = self.__myFont.render(txt[0:LINE_LIM], True, (0,0,0))
                self.__screen.blit(txtImg, Square.getScaledLoc((6.33, 0.33)))
                ##print txt[0:LINE_LIM]
                if 1 < len(txt)/LINE_LIM:
                  txtImg2 = self.__myFont.render(txt[LINE_LIM:LINE_LIM*2], True, (0,0,0))
                  self.__screen.blit(txtImg2, Square.getScaledLoc((7.00, 0.33)))
                  ##print txt[LINE_LIM:LINE_LIM*2]
                i=2
                if len(txt)//LINE_LIM > 2:
                  firstLine = False
                elif len(txt)//LINE_LIM <= 2:
                  eve = True
                
              #print remaining lines:
              elif not(firstLine):
                txtImg = self.__myFont.render(txt[LINE_LIM*i:LINE_LIM*(i+1)], True, (0,0,0))
                self.__screen.blit(txtImg, Square.getScaledLoc((6.33, 0.33)))
                if i+1 < len(txt)/LINE_LIM:
                  txtImg2 = self.__myFont.render(txt[LINE_LIM*(i+1):LINE_LIM*(i+2)], True, (0,0,0))
                  self.__screen.blit(txtImg2, Square.getScaledLoc((7.00, 0.33)))
                i += 2
                if i >= len(txt)//LINE_LIM:
                  firstLine = True
                  eve = True
              ##print eve
              
            elif eve:
              ##print eve
              self.__update()
              eve = False
              ##messagebox.showinfo("Event", \
                      ##self.__myA.getSquare(self.__me.getFacedPos()).getMessage())
               
          if self.__myA.getSquare(self.__me.getCurPos()).isDoor():
            self.__me.setCurPos(self.__myA.getSquare(self.__me.getCurPos()).getLoc2())
            self.__update()

      pygame.display.update()

  def __getMessage(self):
    txt = self.__myA.getSquare(self.__me.getFacedPos()).getMessage()
    '''
    wrds = txt.split()
    i = 0
    start = 0
    lengths = 0
    lines = []
    while i < len(wrds):
      lengths += len(wrds[i]) + 1
      if lengths/LINE_LIM > len(lines)+1:
        lines.append(" ".join(wrds[start:i]))
        start = i
      i += 1
    self.__screen.blit(self.__txtBox, Square.getScaledLoc((6, 0)))
    return lines
    '''
    if len(txt)%LINE_LIM != 0:
      txt += " " * (LINE_LIM-len(txt)%LINE_LIM)
    return txt
    
        
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

  # List should be first row of 2D List returned by __loadArea()
  # Be sure to call __processData AFTER constructing self.__myA
  def __processData(self, L):
    playerAttr = L[0].split()
    self.__PLR_INIT_POS = [int(playerAttr[0]), int(playerAttr[1])]
    self.__PLR_INIT_FACE = int(playerAttr[2])
    for cell in L[1:]:
      pts = cell.split()
      # Info concerning a locked square:
      ##print(pts)
      if len(pts)==3 and pts[2].isdigit():
        self.__myA.getSquare((int(pts[0]),int(pts[1]))).\
                      setLocked(False if int(pts[2])==0 else True)
      if len(pts)>=3 and not(pts[2].isdigit()):
        ##print(" ".join(pts[2:]), self.__myA.getSquare((int(pts[0]),int(pts[1]))))
        self.__myA.getSquare((int(pts[0]),int(pts[1]))).setMessage(" ".join(pts[2:]))
        ##print(self.__myA.getSquare((int(pts[0]),int(pts[1]))).getMessage())
        
      # Info concerning a door's loc2:
      if len(pts)==4 and pts[2].isdigit() and pts[3].isdigit():
        self.__myA.getSquare((int(pts[0]),int(pts[1]))).\
                      setLoc2((int(pts[2]),int(pts[3])))
    
  
  '''
  def main():
    update()
    inp = input("What would you like to do? [w,a,s,d] [q]")
    while inp != "q":
      if inp=="w":
        self.__me.setFacing(Player.N)
        self.__me.move((-1,0))
        ##print("u" + str(self.__me.getCurPos()))
        if self.__myA.getSquare(self.__me.getCurPos()).isWall():
          self.__me.move((1,0))
      elif event.char=="s":
        self.__me.setFacing(Player.S)
        self.__me.move((1,0))
        ##print(self.__me.getCurPos())
        if self.__myA.getSquare(self.__me.getCurPos()).isWall():
          self.__me.move((-1,0))
      elif event.char=="a":
        self.__me.setFacing(Player.E)
        self.__me.move((0,-1))
        ##print(self.__me.getCurPos())
        if self.__myA.getSquare(self.__me.getCurPos()).isWall():
          self.__me.move((0,1))    
      elif event.char=="d":
        self.__me.setFacing(Player.W)
        self.__me.move((0,1))
        ##print(self.__me.getCurPos())
        if self.__myA.getSquare(self.__me.getCurPos()).isWall():
          self.__me.move((0,-1))
      if myA.getSquare(self.__me.getCurPos()).isDoor():
        self.__me.setCurPos(myA.getSquare(self.__me.getCurPos()).getLoc2())
      update()
      inp = input("What would you like to do? [w,a,s,d] [q]")

    #main()
    '''

GUIClass()
