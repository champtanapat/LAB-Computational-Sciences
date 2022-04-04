import matplotlib.pyplot as plt
plt.xlabel('X')   #แกน x พร้อมตั้งชื่อในวงเล็บ
plt.ylabel('Y')   #แกน y พร้อมตั้งชื่อในวงเล็บ


plt.axis([-10, 10, -10, 10])

x = [1,2,3,2,1]
y = [-1,-2,-1,0,-1]

plt.plot(x,y) 
plt.show() 