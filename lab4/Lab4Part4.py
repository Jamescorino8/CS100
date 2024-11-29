#James Corino 5/10/21
import math
size = int(input("Please enter the size of the tile as an integer:  "))
span = int(input("Please enter the length of the span as an integer:  "))

print("")

gap = size / 2
totaltiles = span // size
if totaltiles % 2 == 0:
  totaltiles = totaltiles - 1
int(totaltiles)
whitetiles = totaltiles // 2
int(whitetiles)
blacktiles = totaltiles - whitetiles
int(blacktiles)

print("Number of black tiles needed:  ", blacktiles)
print("Number of white tiles needed:  ", whitetiles)
print("Total number of tiles needed:  ", totaltiles)
print("Gap at each end:", gap)