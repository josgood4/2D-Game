import pickle
from testClass import *

myA = area()
myMap1 = map1(myA)
myMap1.test()

pickle.dump(myMap1, open("myA.p", "wb"))

myA.addEle()
myMap2 = map1(myA)
myMap2.test()
pickle.dump(myMap2, open("myA2.p", "wb"))

myA.addEle()
myA.test()

myM = pickle.load(open("myA.p", "rb"))
myM.test()

myM = pickle.load(open("myA2.p", "rb"))
myM.test()
