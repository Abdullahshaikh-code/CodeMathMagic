# ***Numerical Differentation***
from turtle import end_fill


def  y(x):
    z= x**2+3*x-10
    return z

def derivative(y1,y2,x1,x2):
    d=(y2-y1)/(x2-x1)
    return d
   
print(""" 1.forwor formula
2.backword formula
3.central formula""")
a= int(input("enter 1,2,3:"))
x1=3.228
delta=21
x=x1
y1=y(x)
if a==1:
     x2=x1+delta
     x=x2
     y2=y(x)
     secent=derivative(y1,y2,x1,x2)
     print ("secent=",secent)    
if a==2:
     x2=x1-delta
     x=x2
     y2=y(x)
     secent=derivative(y1,y2,x1,x2)
     print ("secent=",secent)
if a==3:
      x1+=delta
      x=x1
      y1=y(x)
      x2=x1-delta   
      x=x2
      y2=y(x)
      secent=derivative(y1,y2,x1,x2)
      print ("secent=",secent)
else:
  print("enter menu numbers")