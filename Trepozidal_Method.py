from math import sqrt
import math
def f(x):
   fx=1/sqrt(1 +x**2)
   return fx   
a=float(input("enter lower limit"))
b=float(input("enter upper limit"))
n=int(input("enter number of trepozoids"))
h=0.2
if (a<b) :
   x=a
   y= f(x)
   s=y
   sum=0
   for i in range (n-1) :
     x+=h
     y1=f(x)
     sum=(sum+y1)
   sum*=2  
   x+=h
   y=f(x)
   s+=y
   ad=s+sum
   area=(h/2)*ad
   print (area)
else:
    print ("enter correct uppper and lower limi t")   