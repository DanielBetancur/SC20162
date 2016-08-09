#  DAte 09/07/2016
#Este codigo soloucionara el mapeo dinamico logico 
#autor: Daniel Betancur 
import numpy as np
import matplotlib.pyplot as plt
r = 3.8 #Cree las variables basicas para poder empezar a asginar valores y trabajar con ellos 
Nmax = 500
x0 = 0.1

n= np.zeros(Nmax+1)

n[0] = x0
print x0

x= np.zeros(Nmax+1)

for i in range(1,Nmax+1):
		
	y=r*x0*(1-x0)
	x0=y	
	x[i]= x0
	n[i]=i	
	
print x,n
plt.plot(n,x)
plt.show()
