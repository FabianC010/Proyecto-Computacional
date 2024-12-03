#!/usr/bin/env python

import numpy as np
import scipy.sparse as sp
import Hamiltoniano as hm
import Diag as dg
import rk4 as rk
import calculo_norma as cn
import simulacion as sm
import cProfile

##################################################################################################################################################

# Tutorial 

#psiT, hamiltonianoT, timesT, hT = sm.inicializacion(100, 2.0, 1.0, 20.0, 1000)

# Método de RK4
#stateQuantRkT = sm.simulacion_Rk(psiT, hamiltonianoT, timesT, hT) 

# Método de Diagonalización
#stateQuantDiagT = sm.simulacion_Diag(psiT, hamiltonianoT, timesT, hT)

##################################################################################################################################################

# Resultado 1

#psi1, hamiltoniano1, times1, h1 = sm.inicializacion(1500, 10.0, 1.0, 60.0, 1000)

#stateQuant11 = sm.simulacion_Rk(psi1, hamiltoniano1, times1, h1) 

#stateQuant12 = sm.simulacion_Diag(psi1, hamiltoniano1, times1, h1)

##################################################################################################################################################

# Resultado 2

#psi2, hamiltoniano2, times2, h2 = sm.inicializacion(1500, 1.0, 10.0, 60.0, 1000)

#stateQuant21 = sm.simulacion_Rk(psi2, hamiltoniano2, times2, h2)

#stateQuant22 = sm.simulacion_Diag(psi2, hamiltoniano2, times2, h2)

##################################################################################################################################################

# Resultado 3

#psi3, hamiltoniano3, times3, h3 = sm.inicializacion(1500, 5.0, 5.0, 60.0, 1000)

#stateQuant31 = sm.simulacion_Rk(psi3, hamiltoniano3, times3, h3)

#stateQuant32 = sm.simulacion_Diag(psi3, hamiltoniano3, times3, h3)

##################################################################################################################################################

# Resultado 4
 
#epsilon = np.full(1500, 5.0)
#epsilon[600:901] = 15.0
#t_enr = np.full(1499, 5.0)
#psi4 = np.zeros(1500, dtype=complex)
#psi4[1500//2] = 1.0

#times4 = np.linspace(0.0, 60.0, 1000)
#h4 = times4[1] - times4[0]
#hamiltoniano4 = hm.crear_Hamil()

#stateQuant41 = sm.simulacion_Rk(psi4, hamiltoniano4, times4, h4)

#stateQuant42 = sm.simulacion_Diag(psi4, hamiltoniano4, times4, h4)

##################################################################################################################################################

# Resultado 5
 
#epsilon = np.full(1500, 5.0)
#t_enr = np.full(1499, 5.0)
#t_enr[700:781] = 15.0
#psi5 = np.zeros(1500, dtype=complex)
#psi5[1500//2] = 1.0

#times5 = np.linspace(0.0, 60.0, 1000)
#h5 = times5[1] - times5[0]
#hamiltoniano5 = hm.crear_Hamil()

#stateQuant51 = sm.simulacion_Rk(psi5, hamiltoniano5, times5, h5)

#stateQuant52 = sm.simulacion_Diag(psi5, hamiltoniano5, times5, h5)

#################################################################################################################################################

# Resultado 6
 
#epsilon = np.full(1500, 5.0)
#epsilon[600:901] = 25.0
#t_enr = np.full(1499, 5.0)
#t_enr[700:781] = 5.0
#psi6 = np.zeros(1500, dtype=complex)
#psi6[1500//2] = 1.0

#times6 = np.linspace(0.0, 60.0, 1000)
#h6 = times6[1] - times6[0]
#hamiltoniano6 = hm.crear_Hamil()

#stateQuant61 = sm.simulacion_Rk(psi6, hamiltoniano6, times6, h6)

#stateQuant62 = sm.simulacion_Diag(psi6, hamiltoniano6, times6, h6)
 
##################################################################################################################################################

# Paralelización

#psiP, hamiltonianoP, timesP, hP = sm.inicializacion(5000, 1.0, 1.0, 10.0, 1000)

#cProfile.run('sm.simulacion_Rk(psiP, hamiltonianoP, timesP, hP)')
#cProfile.run('sm.simulacion_Rk(psiP, hamiltonianoP, timesP, hP)')

##################################################################################################################################################
