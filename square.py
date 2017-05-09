import pygame


BLOCK_SIZE = 50
SCALE = 2

class Square():
  FLOOR = 0
  WALL = 1
  DOOR = 2
  ACTION = 3
  ITRACT = 4
  # Squares will be identified by their corresponding filename
  #   MAKE SURE ANY Square IMAGES START WITH ONE OF THE FOLLOWING
  TYP_IMG_L = ["", "", "", "", "", ""]
  TYP_IMG_L[FLOOR] = "floo"
  TYP_IMG_L[WALL] = "wall"
  TYP_IMG_L[DOOR] = "door"
  TYP_IMG_L[ACTION] = "acti"
  TYP_IMG_L[ITRACT] = "inte"

  @classmethod
  def INIT(cls, scrn, imgs):
    cls.__screen = scrn         
    cls.__IMAGES = {}
    for eachImage in imgs:
      cls.__IMAGES[eachImage] = \
          pygame.image.load(eachImage).convert_alpha()


  
  def __init__(self, loc, imgStr):
    self.__loc = loc  #tuple containing coord's of the given square
    self.__image = Square.__IMAGES[imgStr]

  def getImage(self):
    return self.__image
  
  #NOTE: SWITCHED X AND Y HERE vvv
  #  2D_ARRAY[y][x] -> (x,y)
  @classmethod
  def getScaledLoc(cls, tup):
    return ((tup[1]+1)*BLOCK_SIZE, (tup[0]+1)*BLOCK_SIZE)
  
  def isWall(self):
    return False

  def isDoor(self):
    return False

  def getType(self):
    return self.__tp

  def getImgTyp(self):
    return self.__imgTyp

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


class WSquare(Square):
  def isWall(self):
    return True


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

  




##sq = Square(0, (0,0), None)
##print(sq)

