#!/usr/bin/env python
import numpy as np

def exps(eigenValues, h, oldState):
    """Evaluacion del exponencial de los valores diagonales del Hamiltoniano.

       Se evalúa la exponencial según lo indica la solución formal a la ecuación de Schrödinger. En este caso,
       el Hamiltoniano se encuentra en una base donde es diagonal. Por ello, la evaluación se realiza con sus 
       autovalores.

    Examples:
        >>> import numpy as np
        >>> exps(np.array([-1.41473988,  0.39770187,  1.97266549,  4.74988177,  9.29449075]), 1.0, np.array([0.0,  0.0,  1.0,  0.0,  0.0]))
        array([ 0.        +0.j         0.        +0.j        -0.39113927-0.9203315j
                0.        +0.j         0.        -0.j  ])
    
    Args:
        eigenValues (ndarray): Primer argumento. Autovalores de Hamiltoniano inicial.
        h (float): Segundo argumento. Valor del paso temporal del estado anterior al actual.
        oldState (ndarray): Tercer argumento. La daga del estado con la que se va a calcular la daga del nuevo 
                            estado del sistema. 

    Returns:
        ndarray: Devuelve los valores de la daga del estado viejo multiplicados por el exponencial de los valores 
                 de la diagonal del hamiltoniano multiplicador por el paso temporal y el opuesto de la constante 
                 imaginaria.
    """
     
    state = np.exp(-1.0j * eigenValues * h) * oldState     # Se usa * y no np.dot() porque los autovalores se guardan como un 
                                                           # vector, no como una matriz diagonal.
    return state


def sol_Vector(eigenVectors, eigenValues, psi, h):
    """ Evaluación del vector solución correspondiente a la dinámica de un sistema cuántico.

    Esta función realiza el cálculo del vector que dicta la solución formal de la ecuación
    de Schrödinger. En este caso particular, el vector se evalúa en la base del espacio vectorial 
    en la cual el Hamiltoniano es diagonal y luego se convierte a la base original para guardar 
    las entradas adecuadas. 
    
    Examples:
        >>> sol_vector(#PONER EIGENVECTORS np.array(), np.array([-1.41473988,  0.39770187,  1.97266549,  4.74988177,  9.29449075]), np.array([0.0,  0.0,  1.0,  0.0,  0.0]), 1.0)  # Terminar
        []

    Args:
        eigenVectors (ndarray): Primer argumento. Autovectores del Hamiltoniano que describe el comportamiento 
                                del sistema.
        eigenValues (ndarray): Segundo argumento. Autovalores del Hamiltoniano que describe el comportamiento
                               del sistema.
        psi (ndarray): Tercer argumento. Vector que contiene las probabilidades de encontrar al fermión en un
                       espacio de la grilla.
        h (float): Cuarto argumento. Valor del paso temporal del estado anterior al actual.

    Returns:
        psi (ndarray): Vector solución avanzado un paso en tiempo.

    """

    psi = eigenVectors.conjugate().transpose().dot(psi)
    psi_t = exps(eigenValues, h, psi)
    psi = eigenVectors.dot(psi_t)

    return psi



