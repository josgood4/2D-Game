class Player():
  def __init__(self, curPos):
    self.__curPos = curPos   # we need this curPos to be mutable,
                             #   so make sure its a list NOT TUPLE
  def getCurPos(self):
    return self.__curPos

  def setCurPos(self, newPos):
    self.__curPos = newPos

  def move(self, newRelPos):
    self.__curPos[0] = self.__curPos[0] + newRelPos[0]
    self.__curPos[1] = self.__curPos[1] + newRelPos[1]

  # use this to compare a tuple with Player's list
  def isHere(self, pos):
    return self.__curPos[0]==pos[0] and self.__curPos[1]==pos[1]
