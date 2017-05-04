from tkinter import *
from Square import *
from Area import *
from Player import *

#Note: BLOCK_SIZE resides in Square.py
WIN_WIDTH = BLOCK_SIZE*10
WIN_HEIGHT = BLOCK_SIZE*9

PLR_INIT_POS = [1,1]
PLR_INIT_FACE = Player.S

class GUIClass():
  
  def __init__(self):
    self.__master = Tk()
    self.__w = Canvas(self.__master, width=WIN_WIDTH, height=WIN_HEIGHT)
    self.__w.pack()

    PLR_IMAGES = {Player.N:PhotoImage(file="images/playerN.gif"), \
              Player.S:PhotoImage(file="images/playerS.gif"), \
              Player.W:PhotoImage(file="images/playerW.gif"), \
              Player.E:PhotoImage(file="images/playerE.gif")}

    IMAGES = {"floor_dirt":PhotoImage(file="images/floor_dirt.gif"), \
              "wall_rock":PhotoImage(file="images/wall_rock.gif"), \
              "door_ladder_down":PhotoImage(file="images/door_ladder_down.gif"), \
              "door_ladder_up":PhotoImage(file="images/door_ladder_up.gif")}

    Square.INIT(self.__w, IMAGES)

    self.__me = Player(self.__w, PLR_INIT_POS, PLR_INIT_FACE, PLR_IMAGES)
    Area.setPlayer(self.__me)
    self.__myA = Area()
    self.__myA.initTest()

    self.__master.tk.call('tk', 'scaling', 2.0)

    #self.__initAreaDraw()
    self.__update()
    
    self.__master.bind("<Key>", self.key)

    ##TODO: exit mechanism vvv
    while True:
      #self.__master.update_idletasks()
      self.__master.update()

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
         
    if self.__myA.getSquare(self.__me.getCurPos()).isDoor():
      self.__me.setCurPos(self.__myA.getSquare(self.__me.getCurPos()).getLoc2())
    #self.__initAreaDraw()
    self.__update()
      
  # If using __initAreaDraw, switch Player.drawMe() method to alternative method
  # __initAreaDraw() has a static background with moving player
  def __initAreaDraw(self):
    for i in range(20):
      for j in range(10):
        self.__myA.getSquare((i,j)).drawMe((i,j))

    self.__me.drawMe(self.__me.getCurPos())

  # __update() moves the background while keeping the player stationary
  def __update(self):
    curPos = self.__me.getCurPos()
    ##print(self.__myA)
    i0 = 0
    for i in range(curPos[0]-4, curPos[0]+5):
      j0 = 0
      for j in range(curPos[1]-4, curPos[1]+6):
        ##print(j, ", ", i)
        self.__myA.getSquare((i,j)).drawMe((i0, j0))
        j0 += 1
      i0 += 1
    self.__me.drawMe()

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

GUIClass()
