#!/usr/bin/env python

import numpy as np
import scipy.sparse as sp
import time
import Hamiltoniano as hm
import Diag as dg
import rk4 as rk
import calculo_norma as cn
import cProfile
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython import display


epsilon = np.full(1500, 1)
t_enr = np.full(1499, 1)
epsilon[600:900] = 20
psi = np.zeros(1500, dtype=float)
psi[1500//2] = 1.0

hamiltoniano = hm.crear_Hamil(epsilon, t_enr)

times = np.linspace(0.0, 100.0, 10000)
h = times[1] - times[0]

def simulation_1(times, psi, hamiltoniano, h):
    startTime1 = time.time()

    stateQuant1 = np.zeros((times.size, 1500), dtype=complex)

    for tt in range(times.size):
        psi = rk.rk4(rk.dynGenerator, hamiltoniano, psi, h)  # Se calcula el nuevo estado del sistema
        stateQuant1[tt] = cn.norma_Cuadrada(psi)
 
    endTime1 = time.time()
    print("Duración (Simulación 1): ", endTime1 - startTime1)

def simulation_2(times, psi, hamiltoniano, h):

    startTime2 = time.time()

    stateQuant2 = np.zeros((times.size, 1500), dtype=complex)

    hamiltoniano_arr = hamiltoniano.toarray()

    eigVals, eigVecs = np.linalg.eigh(hamiltoniano_arr)

    for tt in range(times.size):
        psi = dg.sol_Vector(eigVecs, eigVals, psi, h)
        stateQuant2[tt] = cn.norma_Cuadrada(psi)
        -
    endTime2 = time.time()
    print("Duración (Simulación 2): ", endTime2 - startTime2)



cProfile.run('simulation_1(times, psi, hamiltoniano, h)') 
cProfile.run('simulation_2(times, psi, hamiltoniano, h)')

#fig = plt.figure()
#line, = plt.plot([])
#plt.xlabel('Estados')
#plt.ylabel('Probabilidad')
#plt.xlim(0, psi.size)
#plt.ylim(0, 1)
#plt.grid(True)
#funcion encargada de conseguir los valores mas nuevos de la animacion
#def animate(frames):
 #   line.set_data(range(psi.size), stateQuant2[frames*skip])
  #  return line,

#skip = 100
#anim = FuncAnimation(fig, animate, frames=(times.size)//skip, interval=42, blit=True)
#video = anim.to_html5_video()
#html = display.HTML(anim.to_html5_video())
#display.display(html)
#plt.close()

