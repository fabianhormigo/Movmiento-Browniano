# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:57:48 2021

@author: fabia
"""
__author__ = "Fabian Hormigo Pereila"
__copyright__ = "Copyright (C) 2021 Fabian Hormigo Pereila"
__license__ = "Public Domain"
__version__ = "1.0"
#Movimiento browniano.Ecuación de Langevin.


import numpy as np
import langevin
from matplotlib import pyplot as plt
import time
inicio = time.time()
dt=0.0001
t=[0]
track=1000
iterations=50000
v=0.8*np.ones([track,1])
x=np.zeros([track,1])
acumuladorx=x
acumuladorv=v
x_median=np.array([0])
v_median=np.array([0.8])
sigmax=np.array([0])
sigmav=np.array([0])
tau=np.array([])
#Creación de trayectorias
for k in range(0,iterations):
    [x,v]=langevin.langevin_2(x,v,dt,track)
    
    xi_median=np.median(x)
    vi_median=np.median(v)
    sigmaxi=np.std(x)
    sigmavi=np.std(v)
    
    #acumulador de salidas
    x_median=np.append(x_median,xi_median)
    v_median=np.append(v_median,vi_median)
    sigmax=np.append(sigmax,sigmaxi)
    sigmav=np.append(sigmav,sigmavi)
    
    
    acumuladorx=np.append(acumuladorx,x,axis=1)
    
    acumuladorv=np.append(acumuladorv,v,axis=1)
    
    t=np.append(t,t[k]+dt)
    
#Módulo de ploteo y extracción de imagenes

#Plot de xmedio mas menos sigmax

xsup=x_median-sigmax
xinf=x_median+sigmax

xmediofig=plt.figure(1)
plt.plot(t,x_median)
plt.plot(t,xsup,color='red')
plt.plot(t,xinf,color='red')

plt.xlabel('Tiempo')
plt.ylabel('X medio')

plt.savefig('Xmedio1.png')
#Plot de vmedio mas menos sigma 

vsup=v_median-sigmav
vinf=v_median+sigmav

vmediofig=plt.figure(2)
plt.plot(t,v_median)
plt.plot(t,vsup,color='red')
plt.plot(t,vinf,color='red')

plt.xlabel('Tiempo')
plt.ylabel('V medio')

plt.savefig('Vmedio1.png')

#Potencial

xpotencial=np.linspace(np.min(x_median),max(x_median),1000)
U1=(xpotencial**2)*0.5+(xpotencial**4)*0.25

potencial=plt.figure(3)

plt.ticklabel_format(style='sci', axis='y')


plt.plot(xpotencial,U1,color='red')


plt.savefig('Potential.png')
#histograma de posiciones
Histograma=plt.figure(4)

plt.hist(x_median,bins=100)
plt.xlabel('X medio')
plt.savefig('Histograma.png')

    
fin = time.time()
tiempoejecucion=fin-inicio
   
   




    
  
   
    
    

    
    

    
    
    
    
   
    
   


