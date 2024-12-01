#!/usr/bin/env python

import numpy as np
import scipy.sparse as sp
import Hamiltoniano as hm
import Diag as dg
import rk4 as rk
import calculo_norma as cn
import simulacion as sm
import cProfile

# Tutorial 
psi, hamiltoniano, times, h = sm.inicializacion(100, 2.0, 1.0, 20.0, 1000)

# Método de RK4
stateQuantSimRkT = sm.simulacion_Rk(psi, hamiltoniano, times, h) 

# Método de Diagonalización
stateQuantSimDiagT = sm.simulacion_Diag(psi, hamiltoniano, times, h)


