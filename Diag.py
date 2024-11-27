#!/usr/bin/env python
import numpy as np
import Hamiltoniano as Hm

def exps(eigenValues, h, oldState):
    """Evaluacion del exponencial de los valores diagonales del hamiltoniano.

    Examples:
        >>> exps(np.array([-1.41473988,  0.39770187,  1.97266549,  4.74988177,  9.29449075]), 1, np.array([0,  0,  1,  0,  0]))
        [ 0.        +0.j         0.        +0.j        -0.39113927-0.9203315j
        0.        +0.j         0.        -0.j  ] 
    
    Args:
        eigValues (ndarray): Autovalores de Hamiltoniano inicial.
        h (float): Valor del paso temporal del estado anterior al actual.
        oldState (ndarray): La daga del estado con la que se va a calcular la daga del nuevo estado del sistema. 

    Returns:
        ndarray: Devuelve los valores de la daga del estado viejo multiplicados por el exponencial de los valores 
               de la diagonal del hamiltoniano multiplicador por el paso temporal y el opuesto de la constante 
               imaginaria.
    """ 
    state = np.exp(-1.0j*eigenValues*h)*oldState # Se usa * y no np.dot() porque los autovalores se guardan como un 
                                                 # vector, no como una matriz diagonal.
    return state


def sol_vector(hamil, psi, h):
    """ Evaluación del vector solución correspondiente a la dinámica de un sistema cuántico.

    Esta función realiza el cálculo del vector que dicta la solución formal de la ecuación
    de Schrödinger. Para En este caso particular, el vector proviene de un Hamiltoniano 
    tridiagonal por lo cuál dicho vector se evalúa en la base del espacio vectorial "tridiagonal" 
    y luego se convierte a la base original para guardar las entradas adecuadas. 
    
    Examples:
        >>> sol_vector()  # Terminar

    Args:
        hamil (ndarray): Hamiltoniano tridiagonal.
        psi (ndarray): vector inicial.
        h (float): Valor del paso temporal del estado anterior al actual.

    Returns:
        psi (ndarray): vector solución 


    """
    eigVals, eigVecs = np.linalg.eigh(hamil)
    psi = eigVecs.conjugate().transpose().dot(psi)      
    # REVISAR - 
    psi_t = exps(eigVals, h, psi)
    psi = eigVecs.dot(psi_t)

    return psi
