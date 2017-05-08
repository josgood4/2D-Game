from tkinter import *
from Square import *
from Area import *
from Player import *
from tkinter import messagebox
import csv
#
# THIS GUIClass2 works with PyGame in Python 2.7
#
#####################################################################
# TODO: implement action (GRASS) Square's             }->locked doors
#       make better instructions for the spreadsheet/an actual template
#       switch to pygame()???
#####################################################################

#Note: BLOCK_SIZE resides in Square.py
WIN_WIDTH = BLOCK_SIZE*10
WIN_HEIGHT = BLOCK_SIZE*9

AREA_FILE = "areas/AreaTest.csv"

class GUIClass():
  
  def __init__(self):
    self.__PLR_INIT_POS = [1,1]
    self.__PLR_INIT_FACE = Player.S
    
    self.__master = Tk()
    self.__w = Canvas(self.__master, width=WIN_WIDTH, height=WIN_HEIGHT)
    self.__w.pack()

    PLR_IMAGES = {Player.N:PhotoImage(file="images/playerN.gif"), \
              Player.S:PhotoImage(file="images/playerS.gif"), \
              Player.W:PhotoImage(file="images/playerW.gif"), \
              Player.E:PhotoImage(file="images/playerE.gif")}

    IMAGES = {"images/floor_dirt.gif":PhotoImage(file="images/floor_dirt.gif"), \
              "images/wall_rock.gif":PhotoImage(file="images/wall_rock.gif"), \
              "images/door_ladder_down.gif":PhotoImage(file="images/door_ladder_down.gif"), \
              "images/door_ladder_up.gif":PhotoImage(file="images/door_ladder_up.gif"), \
              "images/interactive_sign.gif":PhotoImage(file="images/interactive_sign.gif"), \
              "images/interactive_door.gif":PhotoImage(file="images/interactive_door.gif"), \
              "images/door_door.gif":PhotoImage(file="images/door_door.gif"), \
              "images/floor_door_mat.gif":PhotoImage(file="images/floor_door_mat.gif"), \
              "images/wall_black.gif":PhotoImage(file="images/wall_black.gif"), \
              "images/door_black.gif":PhotoImage(file="images/door_black.gif"), \
              "images/wall_table_S.gif":PhotoImage(file="images/wall_table_S.gif"), \
              "images/wall_table_N.gif":PhotoImage(file="images/wall_table_N.gif"), \
              "images/floor_indoors.gif":PhotoImage(file="images/floor_indoors.gif"), \
              "images/floor_door_mat.gif":PhotoImage(file="images/floor_door_mat.gif"), \
              }

    Square.INIT(self.__w, IMAGES)
    
    areaInfo = self.__loadArea()
    self.__myA = Area(areaInfo[1:])  #first row contains other data
    self.__processData(areaInfo[0])
    #self.__myA.initTest()
    
    self.__me = Player(self.__w, self.__PLR_INIT_POS, self.__PLR_INIT_FACE, PLR_IMAGES)
    Area.setPlayer(self.__me)

    self.__master.tk.call('tk', 'scaling', 2.0)
    #self.__oldUpdate()
    self.__update()
    self.__master.bind("<Key>", self.key)

    mainloop()

    '''
    ##TODO: exit mechanism vvv
    while True:
      #self.__master.update_idletasks()
      self.__master.update()
    '''

  def key(self, event):
    ##print(self.__me.getCurPos())
    if event.char=="w":
      self.__me.setFacing(Player.N)
      self.__me.move((-1,0))
      if self.__myA.getSquare(self.__me.getCurPos()).isWall():
         self.__me.move((1,0))
         
    elif event.char=="s":
      self.__me.setFacing(Player.S)
      self.__me.move((1,0))
      if self.__myA.getSquare(self.__me.getCurPos()).isWall():
        self.__me.move((-1,0))
         
    elif event.char=="a":
      self.__me.setFacing(Player.W)
      self.__me.move((0,-1))
      if self.__myA.getSquare(self.__me.getCurPos()).isWall():
        self.__me.move((0,1))
         
    elif event.char=="d":
      self.__me.setFacing(Player.E)
      self.__me.move((0,1))
      if self.__myA.getSquare(self.__me.getCurPos()).isWall():
        self.__me.move((0,-1))

    if event.char=="e":
      if self.__myA.getSquare(self.__me.getFacedPos()).getMessage():
        ##print(self.__myA.getSquare(self.__me.getFacedPos()).getMessage())
        messagebox.showinfo("Event", \
                self.__myA.getSquare(self.__me.getFacedPos()).getMessage())
         
    if self.__myA.getSquare(self.__me.getCurPos()).isDoor():
      self.__me.setCurPos(self.__myA.getSquare(self.__me.getCurPos()).getLoc2())
    #self.__oldUpdate()
    self.__update()
      
  # If using __oldUpdate, switch Player.drawMe() method to alternative method
  # __oldUpdate() has a static background with moving player
  def __oldUpdate(self):
    for i in range(20):
      for j in range(10):
        self.__myA.getSquare((i,j)).drawMe((i,j))

    self.__me.drawMe(self.__me.getCurPos())

  # __update() moves the background while keeping the player stationary
  def __update(self):
    curPos = self.__me.getCurPos()
    ##print(self.__myA)
    i0 = 0
    for i in range(curPos[0]-4, curPos[0]+4):
      j0 = 0
      for j in range(curPos[1]-4, curPos[1]+5):
        ##print(j, ", ", i)
        self.__myA.getSquare((i,j)).drawMe((i0, j0))
        j0 += 1
      i0 += 1
    self.__me.drawMe()

  def __loadArea(self):
    f = open(AREA_FILE)
    reader = csv.reader(f)
    
    rows = []
    for line in reader:
      rows.append(line)

    f.close()
    return rows

  # List should be first row of 2D List returned by __loadArea()
  # Be sure to call __processData AFTER constructing self.__myA
  def __processData(self, L):
    playerAttr = L[0].split()
    self.__PLR_INIT_POS = [int(playerAttr[0]), int(playerAttr[1])]
    self.__PLR_INIT_FACE = int(playerAttr[2])
    for cell in L[1:]:
      pts = cell.split()
      # Info concerning a locked square:
      ##print(pts)
      if len(pts)==3 and pts[2].isdigit():
        self.__myA.getSquare((int(pts[0]),int(pts[1]))).\
                      setLocked(False if int(pts[2])==0 else True)
      if len(pts)>=3 and not(pts[2].isdigit()):
        ##print(" ".join(pts[2:]), self.__myA.getSquare((int(pts[0]),int(pts[1]))))
        self.__myA.getSquare((int(pts[0]),int(pts[1]))).setMessage(" ".join(pts[2:]))
        ##print(self.__myA.getSquare((int(pts[0]),int(pts[1]))).getMessage())
        
      # Info concerning a door's loc2:
      if len(pts)==4 and pts[2].isdigit() and pts[3].isdigit():
        self.__myA.getSquare((int(pts[0]),int(pts[1]))).\
                      setLoc2((int(pts[2]),int(pts[3])))
    
  
  '''
  def main():
    update()
    inp = input("What would you like to do? [w,a,s,d] [q]")
    while inp != "q":
      if inp=="w":
        self.__me.setFacing(Player.N)
        self.__me.move((-1,0))
        ##print("u" + str(self.__me.getCurPos()))
        if self.__myA.getSquare(self.__me.getCurPos()).isWall():
          self.__me.move((1,0))
      elif event.char=="s":
        self.__me.setFacing(Player.S)
        self.__me.move((1,0))
        ##print(self.__me.getCurPos())
        if self.__myA.getSquare(self.__me.getCurPos()).isWall():
          self.__me.move((-1,0))
      elif event.char=="a":
        self.__me.setFacing(Player.E)
        self.__me.move((0,-1))
        ##print(self.__me.getCurPos())
        if self.__myA.getSquare(self.__me.getCurPos()).isWall():
          self.__me.move((0,1))    
      elif event.char=="d":
        self.__me.setFacing(Player.W)
        self.__me.move((0,1))
        ##print(self.__me.getCurPos())
        if self.__myA.getSquare(self.__me.getCurPos()).isWall():
          self.__me.move((0,-1))
      if myA.getSquare(self.__me.getCurPos()).isDoor():
        self.__me.setCurPos(myA.getSquare(self.__me.getCurPos()).getLoc2())
      update()
      inp = input("What would you like to do? [w,a,s,d] [q]")

    #main()
    '''

GUIClass()
