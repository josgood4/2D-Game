from tkinter import *
from Square import *
from Area import *
from Player import *

WIN_WIDTH = 600
WIN_HEIGHT = BLOCK_SIZE*(10+1)

master = Tk()
w = Canvas(master, width=WIN_WIDTH, height=WIN_HEIGHT)
w.pack()

PLR_IMAGES = {Player.N:PhotoImage(file="images/playerN.gif"), \
              Player.S:PhotoImage(file="images/playerS.gif"), \
              Player.W:PhotoImage(file="images/playerW.gif"), \
              Player.E:PhotoImage(file="images/playerE.gif")}
IMAGES = {0:PhotoImage(file="images/floor_dirt.gif"), \
          1:PhotoImage(file="images/wall_rock.gif"), \
          2:PhotoImage(file="images/wall_rock.gif")}
Square.INIT(w, IMAGES)

me = Player(w, [2,2], Player.E, PLR_IMAGES)
Area.setPlayer(me)
myA = Area()
myA.initTest()

master.tk.call('tk', 'scaling', 2.0)
for i in range(10):
  for j in range(20):
    myA.getSquare((i,j)).drawMe()

me.drawMe()


mainloop()
