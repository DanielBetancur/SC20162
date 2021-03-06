#Autor Michael Daniel Betancur
#primera tarea Entregable del programa de computacion cientifica 
#Lunes 19 de Septiembre 2016
#Este programa resuelve un problema de creaccion de galaxcias cob numeros aleatorios 
import numpy as np
from math import *
import matplotlib.pyplot as mp
#Archivos para realizar procesos matrmaticos de listas y imprecion de funciones 
#para realizar la solucion de f(x)-miu=0 se usara el metdo de newton crabson 
def evaluafx(x,miu): # esto evalua la fncion en f(x) asignandole un miu que sea enviada  
	x=1-exp(-x)*(x+1)-miu#
	return x
def evaluadx(x,miu):
	x=exp(-x)*x-2*exp(x)#esta evalua la fucion derivada que es un proceso de runge kutta
	return x
teta=[]#Guardara los tetas Aleatorios 
xa=[]#Guardara los xa resultados de la formula 
for i in range (0,10000):
	n=0#tengo que iniciar el n dentro del ciclo para que se resete cada que se corra  
	x=0.9	#tengo que iniciar el x dentro del ciclo para que se resete cada que se corra  ademas le puedo asiignar cuaquier valor de comienzo por que así se define el teorema  este x es el del teorem
	a=np.random.uniform(0,1) # Este proceso crea una miu alaeatoria entre 1 y 2
	Tet=np.random.uniform(0,2*pi) #Este proceso crea una teta alaeatoria en detre 1 y 2pi
	while abs(evaluafx(x,a))>10**(-10):#el while se encarga de evaluar la funcion con el nuevo x y verificar que tan aroximado a cero es
		n+=1		
		x=x-(evaluafx(x,a)/evaluadx(x,a)) #el proceso que evalua el teorema que es	x=x-(f(x)/f'(x)
 	xa.append(x) #Una vez encuentre el x que hace la funcion cero lo guarda en esta variable 
	teta.append(Tet) #gurada teta

y=xa*np.cos(teta)#uso de vectorizacion para generar los nuevos vectores 
x=xa*np.sin(teta)
mp.scatter(y,x)
mp.show()
