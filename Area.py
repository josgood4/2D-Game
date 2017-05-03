from Square import *

class Area():
  @classmethod
  def setPlayer(cls, plr):
    Area.__player = plr

  def __init__(self):
    self.__areaL = []

  def getSquare(self, tup):
    return self.__areaL[tup[0]][tup[1]]

  def initTest(self):
    LENGTH = 10 #make sure this is >3
    ROOM2_START = LENGTH*3//2-2
    # room 1:
    for i in range(LENGTH):
      self.__areaL.append([])
      for j in range(LENGTH):
        self.__areaL[i].append(Square(
          Square.WALL if (i==0 or i==LENGTH-1 or j==0 or j==LENGTH-1) else Square.FLOOR, (i,j), 0))
    self.__areaL[LENGTH-1][LENGTH-3] = DSquare(Square.DOOR, (LENGTH-1, LENGTH-3), 1, (1,ROOM2_START+3))

    # room 2:
    for i in range(LENGTH):
      for j in range(LENGTH, ROOM2_START+LENGTH):
        self.__areaL[i].append(Square(
          Square.WALL if (i==0 or i==LENGTH-1 or j==1 or j==ROOM2_START+LENGTH-1) else Square.FLOOR,\
          (i,j), 0))
    self.__areaL[0][ROOM2_START+3] = DSquare(Square.DOOR, (0,ROOM2_START+3), 1, (LENGTH-2, LENGTH-3))

  def __str__(self):
    retStr = ""
    for i in range(len(self.__areaL)):
      for j in range(len(self.__areaL[i])):
        if not Area.__player.isHere((i,j)):
          retStr += str(" " if self.__areaL[i][j].getType()==Square.FLOOR \
                        else self.__areaL[i][j].getType()) #+ "\t"
        else:
          retStr += str(Area.__player) #+ "\t"
      retStr += "\n"
    return retStr

"""
myA = Area()
myA.initTest()
print(myA)
"""
