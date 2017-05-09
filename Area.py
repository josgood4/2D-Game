from Square import *

PADDING = 5

class Area():
  @classmethod
  def INIT(cls, scrn, plr):
    cls.__screen = scrn
    cls.__player = plr

  def __init__(self, L):
    self.__absAreaL = []
    for i in range(len(L)):
      self.__absAreaL.append([])
      for j in range(len(L[0])):
        ##print i, " ", j
        if L[i][j][7:11]==Square.TYP_IMG_L[Square.DOOR]:
          self.__absAreaL[i].append(DSquare((i,j), L[i][j]))
        elif L[i][j][7:11]==Square.TYP_IMG_L[Square.ITRACT]:
          self.__absAreaL[i].append(ISquare((i,j), L[i][j]))
        elif L[i][j][7:11]==Square.TYP_IMG_L[Square.ACTION]:
          self.__absAreaL[i].append(ASquare((i,j), L[i][j]))
        elif L[i][j][7:11]==Square.TYP_IMG_L[Square.WALL]:
          ##print WSquare((i,j), L[i][j])
          self.__absAreaL[i].append(WSquare((i,j), L[i][j]))
        else:
          self.__absAreaL[i].append(Square((i,j), L[i][j]))

        self.__rects = []
      for i in range(9):    #height of screen (in blocks)
        self.__rects.append([])
        for j in range(10): #width of screen (in blocks)
          self.__rects[i].append(
            pygame.Rect(Square.getScaledLoc((i,j)), \
                        (BLOCK_SIZE, BLOCK_SIZE)) )
    # copy problems??? - use deepcopy() if necessary

  def drawArea(self):
    curPos = Area.__player.getCurPos()
    i0 = 0
    for i in range(curPos[0]-4, curPos[0]+4):
      j0 = 0
      for j in range(curPos[1]-4, curPos[1]+5):
        Area.__screen.blit(self.getSquare((i,j)).getImage(), \
                           self.__rects[i0][j0])
        j0 += 1
      i0 += 1

  def getSquare(self, tup):
    return self.__absAreaL[tup[0]][tup[1]]

  """
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
      self.__absAreaL.append([])
      for j in range(LENGTH+PADDING):
        if (i==0 or i>LENGTH or j==0 or j>LENGTH):
          self.__absAreaL[i].append(Square((i,j), "images/wall_rock.gif"))
        else:
          self.__absAreaL[i].append(Square((i,j), "images/floor_dirt.gif"))
    self.__absAreaL[LENGTH+1][LENGTH-3] = \
        DSquare((LENGTH+1, LENGTH-3), "images/door_ladder_down.gif", \
                (1, 2*LENGTH+PADDING-2))

    # room 2:
    for i in range(LENGTH+PADDING):
      for j in range(LENGTH+PADDING, 2*LENGTH+2*PADDING):
        if (i==0 or i>LENGTH or j==LENGTH+PADDING or j>2*LENGTH+PADDING):
          self.__absAreaL[i].append(Square((i,j), "images/wall_rock.gif"))
        else:
          self.__absAreaL[i].append(Square((i,j), "images/floor_dirt.gif"))
          
    self.__absAreaL[0][2*LENGTH+PADDING-2] = \
        DSquare((0,2*LENGTH+PADDING-2), "images/door_ladder_up.gif", \
                (LENGTH, LENGTH-3))
  """
  def __str__(self):
    retStr = ""
    for i in range(len(self.__absAreaL)):
      for j in range(len(self.__absAreaL[i])):
        if not Area.__player.isHere((i,j)):
          retStr += str(" " if self.__absAreaL[i][j].getType()==Square.FLOOR \
                        else self.__absAreaL[i][j].getType()) #+ "\t"
        else:
          retStr += str(Area.__player) #+ "\t"
      retStr += "\n"
    return retStr

"""
myA = Area()
myA.initTest()
print(myA)
"""
