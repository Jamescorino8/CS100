#James Corino 5/6/21
import math
#The measures of the a particular rectangle are given below in inches.
length = 214
width = 132

#Calculate each of the following for the rectangle.
is_a_square = False
if length == width:
  is_a_square = True
perimeter = length + length + width + width
area = length*width
length_of_diagonal = math.sqrt(width ** 2 + length ** 2)
isGolden = False
if length_of_diagonal == (1 + 5 ** 0.5) / 2:
  isGolden = True

#Print all of the information about the rectangle.
#Its dimensions.
print("This rectangle is 214 inches by 132 inches.")
#Whether it is a square.
if is_a_square == False:
    print("This is not a square.")
else:
    print("this is a square.")
#Its perimeter.
print("The perimeter is", perimeter, "inches.")
#Its area.
print("The are is", area, "square inches.")
#The length of its diagonal.
print("The length of the diagonal is", length_of_diagonal, "inches.")
#Whether it is a golden rectangle.
if isGolden == False:
    print("This rectangle is not Golden.")
else:
    print("This rectangle is Golden.")