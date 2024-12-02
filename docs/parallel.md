# Paralelización

La escalabilidad de un programa en python se hace apartir de las bibliotecas precompiladas como numpy o bibliotecas externas.

![aceleracion rk4](https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/RK4_aceleracion.png)

El método de RK4 tiene una escalabilidad baja y se mantiene casi constante después de 2 hilos, el proceso más intensivo que puede limitar la aceleración del proceso es el producto matriz-vector de dyn_Generator

    return -1.0j * oper.dot(state)

dado que la función `rk4` invoca a la operación `.dot()` cuatro veces cada vez que se ejecuta, la aceleración está limitada por este proceso. 

![aceleracion diagonalizacion](https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/Dg_aceleracion.png)

La escalabilidad del método de diagonalización decrece conforme se aumenta el numero de hilos, esto puede estar dado por un conflicto de los recursos de la computadora y la distribución de trabajo entre los hilos. Además, el manejo de la coordinación de los hilos (los cuales son manejados automáticamente por OMP) puede superar los beneficios que ofrece la paralelización por memoria distribuida. 
La funcion que ocupa de mayores recursos es el producto punto entre psi y eigenvector.
    
    psi = eigenVectors.conjugate().transpose().dot(psi)
    psi_t = exps(eigenValues, h, psi)
    psi = eigenVectors.dot(psi_t)

Aunque el costo computacional es significativo y requiere su tiempo, el método de diagonalización nos da la solución más aproximada a la dinámica real del sistema, gracias a las características del Hamiltoniano. 
