from Square import *
from Area import *
from Player import *

def main():
  ##COMMENT OUT LINE IN __init__ OF Square CLASS BEFORE RUNNING
  Square.INIT(0)
  me = Player([2,2])
  Area.setPlayer(me)
  myA = Area()
  myA.initTest()

  print(myA)  
  inp = input("What would you like to do? [w,a,s,d] [q]")
  while inp != "q":
    if inp=="w":
      me.setFacing(Player.N)
      me.move((-1,0))
      ##print("u" + str(me.getCurPos()))
      if myA.getSquare(me.getCurPos()).isWall():
        print("moving back now")
        me.move((1,0))
    elif inp=="s":
      me.setFacing(Player.S)
      me.move((1,0))
      ##print(me.getCurPos())
      if myA.getSquare(me.getCurPos()).isWall():
        me.move((-1,0))
    elif inp=="a":
      me.setFacing(Player.E)
      me.move((0,-1))
      ##print(me.getCurPos())
      if myA.getSquare(me.getCurPos()).isWall():
        me.move((0,1))    
    elif inp=="d":
      me.setFacing(Player.W)
      me.move((0,1))
      ##print(me.getCurPos())
      if myA.getSquare(me.getCurPos()).isWall():
        me.move((0,-1))
    if myA.getSquare(me.getCurPos()).isDoor():
      me.setCurPos(myA.getSquare(me.getCurPos()).getLoc2())
        
    print(myA)
    inp = input("What would you like to do? [w,a,s,d] [q]")

main()
