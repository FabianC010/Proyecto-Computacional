# Explicación

## Tight Binding


## Sistema
La dinámica de un estado puro para un sistema cuántico aislado se rige bajo la ecuación de Schrödinger ($\hbar = 1$)

\begin{equation}
\frac{\partial}{\partial t} |\psi(t)\rangle = -i \hat{H} |\psi(t)\rangle
\end{equation}

cuya solución formal está dada por

\begin{equation}
|\psi(t)\rangle = e^{-i \hat{H}(t - t_0)} |\psi(t = t_0)\rangle
\end{equation}

Con esto dicho, es necesario resolver de manera numérica la primera ecuación diferencial o evaluar de alguna forma la exponencial de la matriz que se encuentra en la segunda ecuación. Para este proyecto se usan 2 metodologías: **RK4** para la ecuación diferencial y **Diagonalización** para la exponencial.

## ¿Por qué implementar los métodos?

### Runge-Kutta de orden 4
El método de Runge-Kutta de orden 4 (_rk4_) blah blah ESPINES ERROR 

### Diagonalización. 
Por otro lado, al estar trabajando con un Hamiltoniano tridiagonal blah blah
