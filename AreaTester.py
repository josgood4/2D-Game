from square import *
from Area import *
from Player import *

def main():
  me = Player([2,2])
  Area.setPlayer(me)
  myA = Area()
  myA.initTest()

  print(myA)  
  inp = input("What would you like to do? [u,d,l,r] [q]")
  while inp != "q":
    if inp=="u":
      me.move((-1,0))
      ##print("u" + str(me.getCurPos()))
      if myA.getSquare(me.getCurPos()).isWall():
        print("moving back now")
        me.move((1,0))
    elif inp=="d":
      me.move((1,0))
      ##print(me.getCurPos())
      if myA.getSquare(me.getCurPos()).isWall():
        me.move((-1,0))
    elif inp=="l":
      me.move((0,-1))
      ##print(me.getCurPos())
      if myA.getSquare(me.getCurPos()).isWall():
        me.move((0,1))    
    elif inp=="r":
      me.move((0,1))
      ##print(me.getCurPos())
      if myA.getSquare(me.getCurPos()).isWall():
        me.move((0,-1))
        
    print(myA)
    inp = input("What would you like to do? [u,d,l,r] [q]")

main()
