from tkinter import *

BLOCK_SIZE = 50
SCALE = 2

class Square():
  FLOOR = 0
  WALL = 1
  DOOR = 2
  GRASS = 3

  @classmethod
  def INIT(cls, canvas, imgs):
    cls.__canvas = canvas # a tkinter Canvas type
    cls.__IMAGES = imgs   # a dictionary of ###:"image_name"

  
  def __init__(self, tp, loc, imgTyp):
    self.__tp = tp   #type of square - this needs to be a bunch of constants
    self.__loc = loc #tuple containing coord's of the given square
    self.__imgTyp = tp 
    #comment this ^^ out if running AreaTester.py

  
  #NOTE: SWITCHED X AND Y HERE vvv
  #  2D_ARRAY[y][x] -> (x,y)
  @classmethod
  def getScaledLoc(cls, tup):
    return ((tup[1]+1)*BLOCK_SIZE, (tup[0]+1)*BLOCK_SIZE)
  
  def isWall(self):
    return self.__tp == Square.WALL

  def isDoor(self):
    return False

  def getType(self):
    return self.__tp

  # Be sure to call Square.INIT() before running
  # Draw the square at given coord (un-scaled)
  def drawMe(self, tup):
    Square.__canvas.create_image(Square.getScaledLoc(tup), image=Square.__IMAGES[self.__imgTyp])

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




class DSquare(Square):
  def __init__(self, tp, loc, img, loc2):
    Square.__init__(self, tp, loc, img)
    self.__loc2 = loc2   # the location where the door teleports the player

  def getLoc2(self):
    return self.__loc2

  def isDoor(self):
    return True




class LDSquare(DSquare, LSquare):
  def __init__(self, tp, loc, img, loc2, isL):
    DSquare.__init__(self, tp, loc, img, loc2)  
    self.setLocked(isL)



##sq = Square(0, (0,0), None)
##print(sq)

