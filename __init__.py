"""Modelo de Tight Binding de ocupación simple con potencial definido: dinámica

Módulos exportados por este paquete:

-`crear_Hamil: Generador de un Hamiltoniano tridiagonal de dimensión epsilon.size.`
-`exps: Evaluación del exponencial de los valores diagonales del hamiltoniano.`
-`sol_Vector: Evaluación del vector solución correspondiente a la dinámica de un sistema cuántico.`
-`dyn_Generator: Generador de la dinámica de un sistema.`
-`rk4: Implementación del método de Runge-Kutta de orden 4.`
-`norma_cuadrada: Cálculo de la norma al cuadrado de cada componente de un vector.`
-`inicializacion: Crea los parámetros iniciales de un sistema de Tight Binding con un fermión en medio de la grilla. Esta función genera los parámetros iniciales del sistema en el cual, el Hamiltoniano contiene valores
    energéticos homogéneos. Todos los epsilon_i tienen el mismo valor y los t_i tienen el mismo valor ente sí.`
-`simulacion_Rk: Simulación de la evolución temporal de un sistema de Tight Binding utilizando el método de RK4. Se requiere utilizar con inicializacion.`
-`simulacion_Diag: Simulación de la evolución temporal de un sistema de Tight Binding utilizando la diagonalización del Hamiltoniano. Se requiere utilizar con inicialización`
"""
