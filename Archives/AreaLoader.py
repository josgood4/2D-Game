from tkinter import *
from Square import *
from Area import *
from Player import *
from csv import *

f = open("areas/AreaTest.csv")

reader = reader(f)

rows = []
for line in reader:
  rows.append(line)
  ##print(line)

f.close()
