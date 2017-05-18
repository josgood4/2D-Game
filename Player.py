from Square import *
import pygame

class Player():
  # make sure these match the spreadsheet:
  N=0
  S=1
  E=2
  W=3
  REL_POS = {N: (-1, 0), S: (1, 0), \
             W: (0, -1), E: (0, 1)  }
  DEFAULT_INIT_POS = [1,1]
  DEFAULT_INIT_FACING = S
  PLR_POS_ONSCRN = (4,4)
  
  ######################################################
  @classmethod
  def INIT(cls, screen, imgs):
    cls.__screen = screen
    cls.__IMAGES = []
    for eachImage in imgs:
      cls.__IMAGES.append(pygame.image.load(eachImage).convert_alpha())
                             # a dictionary of imgs, where keys coorespond
                             #   to direction player faces
    cls.__rect = pygame.Rect(Square.getScaledLoc(Player.PLR_POS_ONSCRN), \
                            (BLOCK_SIZE, BLOCK_SIZE))
    
  # NOTE: MAKE SURE that you setup Area to set the Player's
  #   initial curPos and facing
  def __init__(self):
    self.__curPos = Player.DEFAULT_INIT_POS   # this is a LIST, NOT TUPLE (needs to be mutable)
    self.__facing = Player.DEFAULT_INIT_FACING
    
  ######################################################
    
  # use this to compare a tuple with Player's curPos
  def isHere(self, pos):
    return self.__curPos[0]==pos[0] and self.__curPos[1]==pos[1]
  
  def getFacing(self):
    return self.__facing

  def setFacing(self, newFace):
    self.__facing = newFace

  def getCurPos(self):
    return self.__curPos

  def setCurPos(self, newPos):
    self.__curPos[0] = newPos[0]
    self.__curPos[1] = newPos[1]

  def getRelFacedPos(self):
    return Player.REL_POS[self.__facing]

  def getFacedPos(self):
    return (Player.REL_POS[self.__facing][0]+self.__curPos[0], \
            Player.REL_POS[self.__facing][1]+self.__curPos[1])

  def getInvRelPos(self):
    return (Player.REL_POS[self.__facing][0]*(-1), \
            Player.REL_POS[self.__facing][1]*(-1))

  ######################################################
  
  def move(self, newRelPos):
    self.__curPos[0] = self.__curPos[0] + newRelPos[0]
    self.__curPos[1] = self.__curPos[1] + newRelPos[1]

  def drawMe(self):
    ##print Player.__IMAGES[self.__facing]
    Player.__screen.blit(Player.__IMAGES[self.__facing], Player.__rect)

  '''
  def getFacedPos(self):
    if self.__facing == Player.N:
      ##print("N")
      return (self.__curPos[0]-1,self.__curPos[1])
    elif self.__facing == Player.S:
      ##print("S")
      return (self.__curPos[0]+1, self.__curPos[1])
    elif self.__facing == Player.W:
      ##print("W")
      return (self.__curPos[0], self.__curPos[1]-1)
    else:
      ##print("E")
      return (self.__curPos[0], self.__curPos[1]+1)

  def getPrevPos(self):
    if self.__facing == Player.N:
      return (self.__curPos[0]+1,self.__curPos[1])
    elif self.__facing == Player.S:
      return (self.__curPos[0]-1, self.__curPos[1])
    elif self.__facing == Player.W:
      return (self.__curPos[0], self.__curPos[1]+1)
    else:
      return (self.__curPos[0], self.__curPos[1]-1)

  # alternative drawMe
  def drawMe(self, tup):
    Player.__screen.create_image(Square.getScaledLoc(self.__curPos), \
                               image=Player.__IMAGES[self.__facing])

  # alternative toString()
  def __str__(self):
    return "Player is at " + str(self.__curPos) + ", facing " + \
      "N" if self.__facing==N else \
      "S" if self.__facing==S else \
      "E" if self.__facing==E else \
      "W"
  '''
  
  def __str__(self):
    return "^" if self.__facing==Player.N else \
           "v" if self.__facing==Player.S else \
           "<" if self.__facing==Player.W else \
           ">"
