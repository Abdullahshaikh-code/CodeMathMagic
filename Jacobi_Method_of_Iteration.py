def iteration(x,y,z,t):
    fx=7+t-3*y-z
    fy=11-9/1*fx-1*z-2*t
    fz=(226-178*fx-1*t-1*fy)/2
    ft=56-7/5*fx-1/9*fz
    return  fx,fy,fz,ft

def eterm(x,x1,y,y1,z,z1,t,t1):
    ex=(x1-x)/x1
    ey=(y1-y)/y1
    ez=(z1-z)/z1
    et=(t1-t)/t1
    return (ex,ey,ez,et)
g=0
x,y,z,t=g,g,g,g
it=iteration(x,y,z,t)
x,y,z,t=it
it_2=iteration(x,y,z,t)
x1,y1,z1,t1=it_2
error_term=eterm(x,x1,y,y1,z,z1,t,t1)
error_x,error_y,error_z,error_t=error_term
totale=error_x+error_y+error_z+error_t
x,y,z,t=x1,y1,z1,t1
i=0
while totale!=0:
   it=iteration(x,y,z,t)
   x,y,z,t=it
   it_2=iteration(x,y,z,t)
   x1,y1,z1,t1=it_2
   error_term=eterm(x,x1,y,y1,z,z1,t,t1)
   error_x,error_y,error_z,error_t=error_term
   totale=error_x+error_y+error_z+error_t
   x,y,z,t=x1,y1,z1,t1
   i+=1
   print(i,".","x=",x1,"y=",y1,"z=",z1,"t=",t1)