from square import *

class Area():
  @classmethod
  def setPlayer(cls, plr):
    Area.player = plr

  def __init__(self):
    self.__areaL = []

  def getSquare(self, tup):
    return self.__areaL[tup[0]][tup[1]]

  def initTest(self):
    LENGTH = 5
    for i in range(LENGTH):
      self.__areaL.append([])
      for j in range(LENGTH):
        self.__areaL[i].append(Square(
          1 if (i==0 or i==LENGTH-1 or j==0 or j==LENGTH-1) else 0, (i,j), None))

  def __str__(self):
    retStr = ""
    for i in range(len(self.__areaL)):
      for j in range(len(self.__areaL[i])):
        if not Area.player.isHere((i,j)):
          retStr += str(self.__areaL[i][j]) + "\t"
        else:
          retStr += "  --ME--  " + "\t"
      retStr += "\n"
    return retStr

"""
myA = Area()
myA.initTest()
print(myA)
"""
