# iteration method

#   4 equations
def iteration(x,y,z,t):
    fx=5+t-2*y-z
    fy=8-3/2*x-2*z-2*t
    fz=(22-4*x-4*t-4*y)/3
    ft=3-2/5*x-1/5*z
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
while totale!=0:
   it=iteration(x,y,z,t)
   x,y,z,t=it
   it_2=iteration(x,y,z,t)
   x1,y1,z1,t1=it_2
   error_term=eterm(x,x1,y,y1,z,z1,t,t1)
   error_x,error_y,error_z,error_t=error_term
   totale=error_x+error_y+error_z+error_t
   print("x=",x1,"y=",y1,"z=",z1,"t=",t1)