import math
def f(x):
    fx= x*x*x-2*x-5
    return fx
import math
a = float(input('First Guess: '))
b = float(input('Second Guess: '))
e=  float(input("tollreable  error"))
x=a
fa=f(x)
x=b
fb=f(x)
f=fa*fb
if f>0:
    print ("better luck next time")
else:
    fc=1
    step=1
    
    while fc!=e:
        c=(a+b)/2
        x=c
        fc=x*x*x-2*x-5
        step=step+1
        f=fa*fc
        
        if (f<0):
             b=c
        else:
            a=c
        print("step=",step, "required root=",c,"f(x)=",fc)
    