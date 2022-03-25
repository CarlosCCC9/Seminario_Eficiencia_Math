# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 23:57:50 2021

@author: UnseR
"""

import numpy as np
import matplotlib.pyplot as plt

n=1000


#Angulo fi aleatorio normal
fi=2*np.pi*np.random.uniform(0,1,n)

#r=3*np.random.uniform(0,1,n) #Radio 3 para pruebas


#Ang thet
#thet=np.pi/2-(0.52*np.random.uniform(0,1,n))
#angulos correctos,  sist. de referencia adecuado


#Angulos producto d ela cinematica
z=2*np.pi*np.random.uniform(0,1,n)
gam=1/(np.sqrt(1-0.9*0.9))
y=np.sin(z)/(gam*((0.9/0.77)+np.cos(z)))


#thet=np.arctan(y)
#thet=np.pi/2-np.arctan(y)
#thet=np.pi-np.arctan(y)
#thet=np.pi/2+np.arctan(y)
l=np.pi/8*np.random.uniform(0,1,n)
thet=np.pi-l-np.pi/2
#thet=np.pi-np.arctan(y)-np.pi/2

#Transf. coord. Cartesianas
x=np.sin(thet)*np.cos(fi)
y=np.sin(thet)*np.sin(fi)
z=np.cos(thet)

#Grafica
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z)
plt.show()
