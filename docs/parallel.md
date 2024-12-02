# Paralelización

La escalabilidad de un programa en python se hace apartir de las bibliotecas precompiladas como numpy o bibliotecas externas.

![aceleracion rk4](https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/RK4_aceleracion.png)

El metodo de RK4 tiene una escalabilidad baja y se mantiene casi constante despues de 2 hilos, el proceso mas intensivo que puede limitar la aceleracion del proceso es producto de matrices de dyn_Generator

    return -1.0j * oper.dot(state)

dado que la funcion rk4 llama esta funcion cuatro veces cada vez que se ejecuta y el coste de la operacion este limita la aceleracion de este.

![aceleracion diagonalizacion](https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/Dg_aceleracion.png)

La escalabilidad del metodo de diagonalizacion decrece conforme se aumenta el numero de hilos, esto se puede dar por un conflicto de los recursos de la computadora y la distribucion de trabajo entre los hilos, ademas que el manejo de la coordinacion de los hilos los cuales son manejados automaticamente por OMP puede superar los beneficios que ofrece la paralelizacion por memoria distribuida. 
La funcion que ocupa de mayores recursos es el producto punto entre psi y eigenvector.
    
    psi = eigenVectors.conjugate().transpose().dot(psi)
    psi_t = exps(eigenValues, h, psi)
    psi = eigenVectors.dot(psi_t)

Aunque el costo computacional es grande este metodo nos da la solucion exacta del sistema
