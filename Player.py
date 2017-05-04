from Square import *

class Player():
  N=0
  S=1
  E=2
  W=3
  PLR_POS_ONSCRN = (4,4)
  def __init__(self, canvas, curPos, facing, imgs):
    self.__canvas = canvas
    self.__curPos = curPos   # we need this curPos to be mutable,
                             #   so make sure its a list NOT TUPLE
    self.__facing = facing
    self.__IMAGES = imgs     # a dictionary of imgs, where keys coorespond
                             #   to direction player faces
  def getCurPos(self):
    return self.__curPos

  def setCurPos(self, newPos):
    self.__curPos[0] = newPos[0]
    self.__curPos[1] = newPos[1]
    
  def getFacing(self):
    return self.__facing

  def setFacing(self, newFace):
    self.__facing = newFace

  def move(self, newRelPos):
    self.__curPos[0] = self.__curPos[0] + newRelPos[0]
    self.__curPos[1] = self.__curPos[1] + newRelPos[1]

  '''
  def drawMe(self, tup):
    self.__canvas.create_image(Square.getScaledLoc(self.__curPos), \
                               image=self.__IMAGES[self.__facing])
  '''
  def drawMe(self):
    self.__canvas.create_image(Square.getScaledLoc(Player.PLR_POS_ONSCRN), \
                               image=self.__IMAGES[self.__facing])

  # use this to compare a tuple with Player's list
  def isHere(self, pos):
    return self.__curPos[0]==pos[0] and self.__curPos[1]==pos[1]

  '''
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
           "<" if self.__facing==Player.E else \
           ">"
