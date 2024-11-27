#!/usr/bin/env python

import numpy as np
import time
import Hamiltoniano as hm
import Diag as dg
import rk4 as rk
import calculo_norma as cn

epsilon = np.full(1500, 1)
t_enr = np.full(1499, 1)
psi = np.zeros(1500, dtype=float)
psi[1500//2] = 1.0

hamiltoniano = hm.crear_Hamil(epsilon, t_enr)

times = np.linspace(0.0, 10.0, 100)
h = times[1] - times[0]

startTime1 = time.time()

stateQuant1 = np.zeros(times.size, dtype = object)

for tt in range(times.size):
    psi = rk.rk4(rk.dynGenerator, hamiltoniano, psi, h) # Se calcula el nuevo estado del sistema
    stateQuant1[tt] = cn.norma_Cuadrada(psi)
    

endTime1 = time.time()
print("Duración: ", endTime1 - startTime1)

######################################################################################################

psi = np.zeros(1500, dtype=float)
psi[1500//2] = 1.0

startTime2 = time.time()

stateQuant2 = np.zeros(times.size, dtype = object)

eigVals, eigVecs = np.linalg.eigh(hamiltoniano)

for tt in range(times.size):
    psi = dg.sol_Vector(eigVecs, eigVals, hamiltoniano, psi, h)
    stateQuant2[tt] = cn.norma_Cuadrada(psi)

endTime2 = time.time()
print("Duración: ", endTime2 - startTime2)
