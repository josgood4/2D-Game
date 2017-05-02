class area:
  def __init__(self):
    self.__my_dict = {"this":1, "is":2, "a":3, "test":4}
    self.__counter = 5

  def addEle(self):
    self.__my_dict[self.__counter] = "yo"
    self.__counter += 1

  def test(self):
    for (k,v) in self.__my_dict.items():
      print("%s  %s" % (k,v))
    print("\n")

class map1:
  def __init__(self, area):
    self.__area = area

  def test(self):
    self.__area.test()
