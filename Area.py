from Square import *
from Player import *
import csv

PADDING = 5

DIR_DICT = {"N":Player.N, "S":Player.S, "W":Player.W, "E":Player.E}

# Squares will be identified by their corresponding filename
#   MAKE SURE ANY Square IMAGES START WITH ONE OF THE FOLLOWING
IMG_CONSTR = {"floo":(lambda x,y,img:  Square((x,y), img)), \
              "wall":(lambda x,y,img: WSquare((x,y), img)), \
              "door":(lambda x,y,img: DSquare((x,y), img)), \
              "acti":(lambda x,y,img: ASquare((x,y), img)), \
              "inte":(lambda x,y,img: ISquare((x,y), img))  }

MISC_FUNC = {"PLRI":(lambda self,i,j,face: \
                     self.setupPlayer(i,j,face)), \
             "LOCK":(lambda self,i,j,b: \
                     self.getSquare((i,j)).setLocked(bool(b))),\
             "MESS":(lambda self,i,j,strList: \
                     self.getSquare((i,j)).setMessage(" ".join(list(strList)))),\
             "LOC2":(lambda self,i,j,tup: \
                     self.getSquare((i,j)).setLoc2((int(tup[0]), int(tup[1]))))
             }

  ######################################################################

class Area():
  
  @classmethod
  def INIT(cls, scrn, imgs):
    cls.__screen = scrn
    
    # IMG_CONSTR_DICT maps the name of every image file
    #    to its corresponding constructor
    cls.__IMG_CONSTR_DICT = {}
    for i in imgs:
      cls.__IMG_CONSTR_DICT[i] = IMG_CONSTR[i[7:11]]

  ######################################################################
  
  def __init__(self, fileName, plr):
    self.__player = plr
    L = self.__loadArea(fileName)
    
    # Setting up the Squares:
    L_SQUARE = L[1:] #ignore first row, as that holds other data
    self.__absAreaL = []
    for i in range(len(L_SQUARE)):   
      self.__absAreaL.append([])
      for j in range(len(L_SQUARE[0])):
        self.__absAreaL[i].append( \
            Area.__IMG_CONSTR_DICT[L_SQUARE[i][j]](i, j, L_SQUARE[i][j]))
        
    # Setting up the Rects:
    self.__rects = []
    for i in range(9):    #height of screen (in blocks)
      self.__rects.append([])
      for j in range(10): #width of screen (in blocks)
        self.__rects[i].append(
          pygame.Rect(Square.getScaledLoc((i,j)), (BLOCK_SIZE, BLOCK_SIZE)))

    # Setting attributes of "special" Squares, as well as setupPlayer()
    #   each "special" attribute is of the form:
    #   FUNC_NAME y_pos x_pos *args
    for cell in L[0]:
      pts = cell.split()
      if len(pts)>3:
        MISC_FUNC[pts[0]](self, int(pts[1]), int(pts[2]), pts[3:])

        
  def __loadArea(self, areaFileName):
    f = open(areaFileName)
    reader = csv.reader(f)
    
    rows = []
    for line in reader:
      rows.append(line)

    f.close()
    return rows


  def setupPlayer(self, y, x, facing):
    self.__player.setFacing(DIR_DICT[facing[0]])
    self.__player.setCurPos([y,x])
        
  ######################################################################        

  def drawArea(self):
    curPos = self.__player.getCurPos()
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

  def __str__(self):
    retStr = ""
    for i in range(len(self.__absAreaL)):
      for j in range(len(self.__absAreaL[i])):
        if not self.__player.isHere((i,j)):
          retStr += str(" " if self.__absAreaL[i][j].getType()==Square.FLOOR \
                        else self.__absAreaL[i][j].getType()) #+ "\t"
        else:
          retStr += str(self.__player) #+ "\t"
      retStr += "\n"
    return retStr

"""
myA = Area()
myA.initTest()
print(myA)
"""

