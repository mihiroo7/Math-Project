import numpy as np
import math

cordi=[]
alp1=math.pi/2+math.pi/8
alp2=math.pi/2+math.pi/8
g=9.8
l1=2
l2=2
m1=10
m2=10

temp=[]

x1=l1*np.sin(alp1)
y1=-1*l1*np.cos(alp1)
x2=l1*np.sin(alp1)+l2*np.sin(alp2)
y2=-1*l1*np.cos(alp1)-1*l2*np.cos(alp2)
p1=0
p2=0
mew=m2/m1

temp.append(x1)
temp.append(y1)
temp.append(x2)
temp.append(y2)
cordi.append(temp)

# for i in range(200000):
#     k=(-1*m2*l2*(alpd2**2)*np.sin((alp1-alp2))-(m1+m2)*g*np.sin(alp1))
#     G=m2*np.cos((alp1-alp2))*(-1*l1*alpd1**2*np.sin((alp1-alp2))+g*np.sin(alp2))
#     d2alp1=(k+G)/((m1+m2)*l1-m2*l1*np.cos((alp1-alp2))**2)
#     d2alp2=(-1*g*np.sin(alp2)+l1*(alpd1**2)*np.sin((alp1-alp2))-l1*d2alp1*np.cos((alp1-alp2)))/l2
#     alp1=alp1+alpd1/1000
#     alp2=alp2+alpd2/1000
#     alpd1=alpd1+d2alp1/1000
#     alpd2=alpd2+d2alp2/1000
#     x1=l1*np.sin(alp1)
#     y1=-1*l1*np.cos(alp1)
#     x2=l1*np.sin(alp1)+l2*np.sin(alp2)
#     y2=-1*l1*np.cos(alp1)-1*l2*np.cos(alp2)
#     temp2=[]
#     temp2.append(x1)
#     temp2.append(y1)
#     temp2.append(x2)
#     temp2.append(y2)
#     cordi.append(temp2)

def f(alp1,alp2,p1,p2,m1,mew,l1):
    ans=[]
    ans.append((p1-p2*np.cos(alp1-alp2))/(m1*(l1**2)*(1+mew*(np.sin(alp1-alp2)**2))))
    A1=(p1*p2*np.sin(alp1-alp2))/(m1*(l1**2)*(1+mew*(np.sin(alp1-alp2)**2)))
    A2=((p1**2*mew-2*p1*p2*mew*np.cos(alp1-alp2)+p2**2*(1+mew))*np.sin(2*(alp1-alp2)))/(2*m1*l1**2*(1+mew*(np.sin(alp1-alp2)**2))**2)
    
    ans.append((p2*(1+mew)-p1*mew*np.cos(alp1-alp2))/(m1*l1**2*(1+mew*(np.sin(alp1-alp2)**2))))
    ans.append(-1*m1*(1+mew)*g*l1*np.sin(alp1)-A1+A2)
    ans.append(-1*m1*mew*g*l1*np.sin(alp2)+A1-A2)    
    return ans
    
    

for i in range(20000):
    fans=f(alp1,alp2,p1,p2,m1,mew,l1)
    
    y1=[]
    for i in fans:
        y1.append(i/100)
        
    y2=f(alp1+y1[0]/2,alp2+y1[1]/2,p1+y1[2]/2,p2+y1[3]/2,m1,mew,l1)
    for i in range(4):
        y2[i]=y2[i]/100
        
    y3=f(alp1+y2[0]/2,alp2+y2[1]/2,p1+y2[2]/2,p2+y2[3]/2,m1,mew,l1)
    for i in range(4):
        y3[i]=y3[i]/100
        
    y4=f(alp1+y3[0],alp2+y3[1],p1+y3[2],p2+y3[3],m1,mew,l1)
    for i in range(4):
        y4[i]=y4[i]/100
        
    alp1=alp1+(y1[0]+2*y2[0]+2*y3[0]+y4[0])/6
    alp2=alp2+(y1[1]+2*y2[1]+2*y3[1]+y4[1])/6
    p1=p1+(y1[2]+2*y2[2]+2*y3[2]+y4[2])/6
    p2=p2+(y1[3]+2*y2[3]+2*y3[3]+y4[3])/6
    
    x1=l1*np.sin(alp1)
    y1=-1*l1*np.cos(alp1)
    x2=l1*np.sin(alp1)+l2*np.sin(alp2)
    y2=-1*l1*np.cos(alp1)-1*l2*np.cos(alp2)
    temp2=[]
    temp2.append(x1)
    temp2.append(y1)
    temp2.append(x2)
    temp2.append(y2)
    cordi.append(temp2)
    
    
    
        
        
    
      
    
    
    



