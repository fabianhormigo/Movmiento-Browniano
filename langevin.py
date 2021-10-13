# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:28:51 2021

@author: fabia
"""
__author__ = "Fabian Hormigo Pereila"
__copyright__ = "Copyright (C) 2021 Fabian Hormigo Pereila"
__license__ = "Public Domain"
__version__ = "1.0"

#Mov.browniano con fuerza externa f


def langevin_1(x_in,v_in,dt,n):
    """Definicion de la funcion de levin con f_e=-x"""

    import numpy
    
    A=0.8
    B=(1.4)**0.5
    
    
    
    vout=v_in-A*v_in*dt+B*numpy.random.normal(0,1,[n,1])*((dt)**0.5)-x_in
    xout=x_in+v_in*dt
    return [xout,vout]

def langevin_2(x_in,v_in,dt,n):
    """Definicion de la funcion de levin con f_e=-x-x^3"""
    import numpy
    A=0.8
    B=(1.4)**0.5

    vout=v_in-A*v_in*dt+B*numpy.random.normal(0,1,[n,1])*((dt)**0.5)-x_in-x_in**3
    xout=x_in+v_in*dt
    return [xout,vout]

def langevin_3(x_in,v_in,dt,n):
    """Definicion de la funcion de levin con f_e=+x-x**3"""
    import numpy
    A=0.8
    B=(1.4)**0.5
   
    vout=v_in-A*v_in*dt+B*numpy.random.normal(0,1,[n,1])*((dt)**0.5)+x_in-x_in**3
    xout=x_in+v_in*dt
    return [xout,vout]

    
    
