import pygame

BLOCK_SIZE = 50
SCALE = 2

class Square():
  FLOOR = 0
  WALL = 1
  DOOR = 2
  ACTION = 3
  ITRACT = 4

  @classmethod
  def INIT(cls, scrn, imgs):
    cls.__screen = scrn         
    cls.__IMAGES = {}
    for eachImage in imgs:
      cls.__IMAGES[eachImage] = \
          pygame.image.load(eachImage).convert_alpha()

  #NOTE: SWITCHED X AND Y HERE vvv
  #  2D_ARRAY[y][x] -> (x,y)
  @classmethod
  def getScaledLoc(cls, tup):
    return ((tup[1])*BLOCK_SIZE, (tup[0])*BLOCK_SIZE)

  ######################################################
  
  def __init__(self, loc, imgStr):
    self.__loc = loc  #tuple containing coord's of the given square
    self.__image = Square.__IMAGES[imgStr]

  def getImage(self):
    return self.__image
  
  def isWall(self):
    return False

  def isDoor(self):
    return False

  def getMessage(self):
    return ""

  '''
  # Be sure to call Square.INIT() before running
  # Draw the square at given coord (un-scaled)
  def drawMe(self, tup):
    self.__screen.blit(self.__IMAGES[self.__tp], \
        pygame.Rect(Square.getScaledLoc(tup), (BLOCK_SIZE, BLOCK_SIZE)))
  '''
  def __str__(self):
    return str(self.__image) + " @ " + str(self.__loc)

######################################################

class WSquare(Square):
  def isWall(self):
    return True

######################################################

class ISquare(Square):
  # ALWAYS CALL setLocked() after calling __init__()
  def __init__(self, loc, img):
    Square.__init__(self, loc, img)
    self.__isLocked = True

  def isWall(self):
    return self.__isLocked

  def setLocked(self, isL):
    self.__isLocked = isL
  
  def setMessage(self, string):
    self.__message = string

  def getMessage(self):
    return self.__message

######################################################

class DSquare(Square):
  # ALWAYS CALL setLoc2() AFTER calling __init__()
  def __init__(self, loc, img):
    Square.__init__(self, loc, img)
    self.__loc2 = [1,1]   # the location where the door teleports the player

  def getLoc2(self):
    return self.__loc2

  def setLoc2(self, loc2):
    self.__loc2 = loc2

  def isDoor(self):
    return True

