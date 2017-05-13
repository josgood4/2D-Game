from Square import *

PADDING = 5

class Area():
  @classmethod
  def INIT(cls, scrn, plr, imgs):
    cls.__screen = scrn
    cls.__player = plr
    cls.__imgs = imgs
    # Squares will be identified by their corresponding filename
    #   MAKE SURE ANY Square IMAGES START WITH ONE OF THE FOLLOWING
    TYP_IMG_L = {"floo":(lambda x,y,img:  Square((x,y), img)), \
                 "wall":(lambda x,y,img: WSquare((x,y), img)), \
                 "door":(lambda x,y,img: DSquare((x,y), img)), \
                 "acti":(lambda x,y,img: ASquare((x,y), img)), \
                 "inte":(lambda x,y,img: ISquare((x,y), img))  }
    cls.__IMG_CONSTR_DICT = {}
    for img in cls.__imgs:
      cls.__IMG_CONSTR_DICT[img] = TYP_IMG_L[img[7:11]]
    # IMG_CONSTR_DICT maps the name of every image file
    #    to its corresponding constructor

  def __init__(self, L):
    # Setting up the Squares:
    L_SQUARE = L[1:] #ignore first row, as that holds other data
    self.__absAreaL = []
    for i in range(len(L_SQUARE)):   
      self.__absAreaL.append([])
      for j in range(len(L_SQUARE[0])):
        self.__absAreaL[i].append(
          Area.__IMG_CONSTR_DICT[L_SQUARE[i][j]](i, j, L_SQUARE[i][j]))
        
    # Setting up the Rects:
    self.__rects = []
      for i in range(9):    #height of screen (in blocks)
        self.__rects.append([])
        for j in range(10): #width of screen (in blocks)
          self.__rects[i].append(
            pygame.Rect(Square.getScaledLoc((i,j)), \
                        (BLOCK_SIZE, BLOCK_SIZE)) )
    # copy problems??? - use deepcopy() if necessary
    
    # Setting up other miscellaneous things:
    # Player Attributes:
    playerAttr = L[0][0].split()
    ##print playerAttr
    self.__PLR_INIT_POS = [int(playerAttr[0]), int(playerAttr[1])]
    self.__PLR_INIT_FACE = int(playerAttr[2])
    
    for cell in L[0][1:]:
      pts = cell.split()
      # Info concerning a locked square:
      ##print(pts)
      if len(pts)==3 and pts[2].isdigit():
        self.getSquare((int(pts[0]),int(pts[1]))).\
                      setLocked(False if int(pts[2])==0 else True)
      if len(pts)>=3 and not(pts[2].isdigit()):
        self.getSquare((int(pts[0]),int(pts[1]))).setMessage(" ".join(pts[2:]))
        
      # Info concerning a door's loc2:
      if len(pts)==4 and pts[2].isdigit() and pts[3].isdigit():
        self.getSquare((int(pts[0]),int(pts[1]))).\
                      setLoc2((int(pts[2]),int(pts[3])))
        

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
