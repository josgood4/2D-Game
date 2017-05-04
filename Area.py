from Square import *

PADDING = 5

class Area():
  @classmethod
  def setPlayer(cls, plr):
    Area.__player = plr

  def __init__(self):
    self.__areaL = []

  def getSquare(self, tup):
    return self.__areaL[tup[0]][tup[1]]

  def initTest(self):
    '''
    # Note: thanks to Python's ability to interpret negative indeces for lists,
    #   padding is only necessary on the lower left sides of a room/area:
    #   (but make sure to have a solid wall on the other sides!!!)
    111111111111111111111112111111
    1          11111          1111
    1          11111          1111
    1          11111          1111
    1          11111          1111
    1          11111          1111
    1          11111          1111
    1          11111          1111
    1       v  11111          1111
    1          11111          1111
    1          11111          1111
    111111121111111111111111111111
    111111111111111111111111111111
    111111111111111111111111111111
    111111111111111111111111111111
    this is the rooms generated with LENGTH=10
    '''
    LENGTH = 5 #make sure this is >3
    ROOM2 = LENGTH*4//2-2
    # room 1:
    for i in range(LENGTH+PADDING):
      self.__areaL.append([])
      for j in range(LENGTH+PADDING):
        if (i==0 or i>LENGTH or j==0 or j>LENGTH):
          self.__areaL[i].append(Square((i,j), "wall_rock"))
        else:
          self.__areaL[i].append(Square((i,j), "floor_dirt"))
    self.__areaL[LENGTH+1][LENGTH-3] = \
        DSquare((LENGTH+1, LENGTH-3), "door_ladder_down", \
                (1, 2*LENGTH+PADDING-2))

    # room 2:
    for i in range(LENGTH+PADDING):
      for j in range(LENGTH+PADDING, 2*LENGTH+2*PADDING):
        if (i==0 or i>LENGTH or j==LENGTH+PADDING or j>2*LENGTH+PADDING):
          self.__areaL[i].append(Square((i,j), "wall_rock"))
        else:
          self.__areaL[i].append(Square((i,j), "floor_dirt"))
          
    self.__areaL[0][2*LENGTH+PADDING-2] = \
        DSquare((0,2*LENGTH+PADDING-2), "door_ladder_up", \
                (LENGTH, LENGTH-3))

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
