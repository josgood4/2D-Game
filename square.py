

class Square():
  FLOOR = 0
  WALL = 1
  DOOR = 2
  GRASS = 3
  
  def __init__(self, tp, loc, img):
    self.__tp = tp   #type of square - this needs to be a bunch of constants
    self.__loc = loc #tuple containing coord's of the given square
    self.__img = img #TO DO
  
  def isWall(self):
    return self.__tp == Square.WALL

  def isDoor(self):
    return False

  def drawMe(self):
    #TO DO
    pass

  def getType(self):
    return self.__tp

  def __str__(self):
    return str(self.__tp) + " @ " + str(self.__loc)

class LSquare(Square):
  def __init__(self, tp, loc, img, isL):
    self.super(tp, loc, img)
    self.__isLocked = isL

  def isWall(self):
    return self.__isLocked

  def setLocked(self, isL):
    self.__isLocked = isL

# NOTE: thus all DSquare's are LSquare's,
#    but not all LSquare's are DSquare's
class DSquare(LSquare):
  def __init__(self, tp, loc, img, loc2, isL=False,):
    self.super(tp, loc, img, isL)
    self.__loc2 = loc2   # the location where the door teleports the player

  def getLoc2(self):
    return self.__loc2

  def isDoor(self):
    return True

  def setLocked(self, isL):
    self.super(isL)

##sq = Square(0, (0,0), None)
##print(sq)

