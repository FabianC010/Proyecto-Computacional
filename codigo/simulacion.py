#!/usr/bin/env python

import numpy as np
import scipy.sparse as sp
import time
import Hamiltoniano as hm
import Diag as dg
import rk4 as rk
import calculo_norma as cn

def inicializacion(tamaño, epsilonValue, tValue, timeFinal, timeDivision):
    """
    Crea los parámetros iniciales de un sistema de Tight Binding con un fermión en medio de la grilla.

    Esta función genera los parámetros iniciales del sistema en el cual, el Hamiltoniano contiene valores
    energéticos homogéneos. Todos los epsilon_i tienen el mismo valor y los t_i tienen el mismo valor ente sí.

    Examples: 
        >>> import numpy as np
        >>> import Hamiltoniano as hm
        >>> inicializacion(5, 1.0, 1.0, 10.0, 5)
        array([0.+0.j 0.+0.j 1.+0.j 0.+0.j 0.+0.j]), <DIAgonal sparse matrix of dtype 'float64'
	with 13 stored elements (3 diagonals) and shape (5, 5)>, array([ 0.   2.5  5.   7.5 10. ]), 2.5
 
    Args: 
        tamaño (int): Primer argumento. Tamaño del Hamiltoniano cuadrado y del vector psi.
        epsilonValue (float): Segundo argumento. Valor energético que es colocado en la diagonal principal
                              del Hamiltoniano.
        tValue (float): Tercer argumento. Valor energético que es colocado en las diagonales secundarias 
                        del Hamiltoniano.
	timeFinal (float): Cuarto argumento. Tiempo final de evaluación del sistema.
        timeDivision (int): Quinto argumento. Cantidad de instantes temporales en los que se quiere dividir el
                            tiempo de estudio del sistema.
        
    Returns:
        psi (ndarray): Vector que contiene a un fermión en el medio. Representa las probabilidades de encontrarlo
                       en un punto de la grilla.
        hamiltoniano (sparse matrix): Matriz dispersa que solo contiene los elementos no nulos del 
                                                Hamiltoniano tridiagonal.
        times (ndarray): Lista que contiene todos los instantes de tiempo separados de manera homogénea.
        h (float): Separación entre los instántes temporales.
    """

    epsilon = np.full(tamaño, epsilonValue)
    t_enr = np.full(tamaño - 1, tValue)
    psi = np.zeros(tamaño, dtype=complex)
    psi[tamaño//2] = 1.0

    times = np.linspace(0.0, timeFinal, timeDivision)
    h = times[1] - times[0]
    hamiltoniano = hm.crear_Hamil(epsilon, t_enr)

    return psi, hamiltoniano, times, h

#print(help(inicializacion))


def simulacion_Rk(psi, hamiltoniano, times, h):
    """
    Simulación de la evolución temporal de un sistema de Tight Binding utilizando el método de RK4.

    Se requiere utilizar con inicializacion

    Examples: 
        >>> import rk4 as rk
        >>> # Inicialización de parámetros
        >>> psi, hamiltoniano, times, h = inicializacion(5, 1.0, 1.0, 10.0, 5)
        >>> simulacion_Rk(psi, hamiltoniano, times, h)
        array([[193.8247680664062 563.9756944444443 755.8856947157117 563.9756944444443 193.8247680664062],
               [1289354.0959715855 3869265.1584578156 5157378.375110836 3869265.1584578147 1289354.0959715855],
               [8786343156.233133 26359141278.332462 35145409065.596016 26359141278.332462 8786343156.233133],
               [59865941087488.94 179597820784174.0 239463762290115.78 179597820784174.0 59865941087488.94],
               [4.078968837688574e+17 1.2236906508230554e+18 1.6315875351315126e+18 1.2236906508230554e+18 4.078968837688574e+17]])
    
    Args:
        psi (ndarray): Vector que contiene a un fermión en el medio. Representa las probabilidades de encontrarlo 
                       en un punto de la grilla.
        hamiltoniano (sparse matrix): Matriz dispersa que representa el Hamiltoniano del sistema.
        times (ndarray): Lista que contiene los tiempos en los que se evalúa el sistema.
        h (float): Paso temporal entre dos instantes de tiempo.

    Returns:
        stateQuant (ndarray): Arreglo que contiene la norma cuadrada de `psi` en cada instante de tiempo.
    """

    stateQuant = np.zeros((times.size, psi.size), dtype=object)

    for tt in range(times.size):
        psi = rk.rk4(rk.dyn_Generator, hamiltoniano, psi, h)
        stateQuant[tt] = cn.norma_Cuadrada(psi)

    return stateQuant

#print(help(simulacion_Rk))


def simulacion_Diag(psi, hamiltoniano, times, h):
    """
    Simulación de la evolución temporal de un sistema de Tight Binding utilizando la diagonalización del Hamiltoniano.

    Esta función evaluá la dinámica de un sistema de Tight Binding mediante la diagonalización de un Hamiltoniano 
    tridiagonal cuadrado. Sin embargo, el Hamiltoniano es una matriz dispersa, por lo que se construye en su totalidad
    para realizar el procedimiento de diagonalización y con ello obtener sus autovalores y autovectores.

    Examples: 
        >>> import Diag as dg
        >>> import calculo_norma as cn
        >>> # Inicialización de parámetros
        >>> psi, hamiltoniano, times, h = inicializacion(5, 1.0, 1.0, 10.0, 5)
        >>> simulacion_Diag(psi, hamiltoniano, times, h)
        array([[0.209464917371582 0.2869519961103885 0.007166173036058706 0.28695199611038824 0.20946491737158227],
               [0.32936579228694557 0.15971060758071676 0.021847200264674668 0.15971060758071634 0.32936579228694557],
               [0.0008713063812095321 0.05642187952834626 0.8854136281808872 0.05642187952834643 0.0008713063812095221],
               [0.1020299126952069 0.3327526922372457 0.1304347901350932 0.3327526922372457 0.1020299126952073],
               [0.4192922095224246 0.03717890618391921 0.08705776858731158 0.03717890618391907 0.41929220952242385]])
    
    Args:
        psi (ndarray): Vector que contiene a un fermión en el medio. Representa las probabilidades de encontrarlo 
                       en un punto de la grilla.
        hamiltoniano (sparse matrix): Matriz dispersa que representa el Hamiltoniano del sistema.
        times (ndarray): Lista que contiene los tiempos en los que se evalúa el sistema.
        h (float): Paso temporal entre dos instantes de tiempo.

    Returns:
        stateQuant (ndarray): Arreglo que contiene la norma cuadrada de `psi` en cada instante de tiempo.
    """

    stateQuant = np.zeros((times.size, psi.size), dtype=object)
    hamiltonianoCompleto = hamiltoniano.toarray()

    eigVals, eigVecs = np.linalg.eigh(hamiltonianoCompleto)

    for tt in range(times.size):
        psi = dg.sol_Vector(eigVecs, eigVals, psi, h)
        stateQuant[tt] = cn.norma_Cuadrada(psi)

    return stateQuant

#print(help(simulacion_Diag))

