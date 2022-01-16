"""
Given x and y as input. Print all the powers of x from 1 to y i.e. x1 x2 x3 x4 ... xn
Input: 
x = 13, y = 2
Output:
13#169#
"""

x = 13
y = 2
pt = "#"
st = ""
for i in range (1, y+1):
  st = str(x**i) + pt
  print(st, end = "")
