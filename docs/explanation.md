# Explicación

## Tight Binding


## Sistema

La dinámica de un estado puro para un sistema cuántico aislado se rige bajo la ecuación de Schrödinger ($\hbar = 1$):

$$
\begin{equation}
\frac{\partial}{\partial t} |\psi(t)\rangle = -i \hat{H} |\psi(t)\rangle
\end{equation},
$$
cuya solución formal está dada por:

$$
\begin{equation}
|\psi(t)\rangle = e^{-i \hat{H}(t - t_0)} |\psi(t = t_0)\rangle
\end{equation}
$$

Con esto dicho, es necesario resolver de manera numérica la primera ecuación diferencial o evaluar de alguna forma la exponencial de la matriz que se encuentra en la segunda ecuación. Para este proyecto se usan 2 metodologías: **RK4** para la ecuación diferencial y **Diagonalización** para la exponencial.

## ¿Por qué implementar los métodos?

### Runge-Kutta de orden 4

El método de Runge-Kutta de orden 4 (_RK4_) evalúa el estado del sistema a partir de un estado anterior en el tiempo, es decir, de forma iterativa. Para ello, utiliza cuatro variables, razón por la que el método es de orden 4. Este orden es el más utilizado ya que corresponde al mejor compromiso entre complejidad y error de aproximación. Más formalmente, este método mejora la aproximación de una ecuación diferencial con el método de Euler sin la necesidad de considerar órdenes más altos en la expansión de Taylor de $y(t+h)$, donde h es un paso temporal. Para ello, usa puntos entre $y(t)$ y $y(t+h)$ para conseguir la aproximación. Luego, calcula la expansión de Taylor de ambas expresiones alrededor de esos puntos, para restarlas y terminar cancelando términos. Al hacer eso, quedan las siguientes ecuaciones: 

$$
\begin{align} 
 k_1 &= h f ( t_n ,\ y_n ) \\
 k_2 &= h f ( t_n + \frac{h}{2} ,\ y_n +\frac{k_1}{2} ) \\
 k_3 &= h f ( t_n + \frac{h}{2} ,\ y_n + \frac{k_2}{2} ) \\
 k_4 &= h f ( t_n + h ,\ y_n + k_3 ) \\
 y_{n + 1} &= y_n + \frac{1}{6} (k_1 + 2 k_2 + 2 k_3 + k_4) , 
\end{align}
$$

donde h es el paso temporal y f es la función que genera la dinámica del problema en cuestión, que en este caso es la ecuación de Schrödinger que vimos anteriormente.

Sin embargo, en el caso de este problema, la dinámica del sistema no depende explícitamente del tiempo. Entonces, las ecuaciones toman la siguiente forma:

$$
\begin{align} 
 k_1 &= h f ( oper ,\ y_n ) \\
 k_2 &= h f ( oper ,\ y_n +\frac{k_1}{2} ) \\
 k_3 &= h f ( oper ,\ y_n + \frac{k_2}{2} ) \\
 k_4 &= h f ( oper ,\ y_n + k_3 ) \\
 y_{n + 1} &= y_n + \frac{1}{6} (k_1 + 2 k_2 + 2 k_3 + k_4) , 
\end{align}
$$

Donde oper representa un operador lineal, que en este problema es el Hamiltoniano.

El error de aproximación es $\mathcal{O}(h^5)$, mientras que el error global es aproximadamente del orden $\mathcal{O}(h^4)$. En este caso, se ataca el problema en la "base de espines" de las partículas involucradas.

### Diagonalización. 

Por otro lado, al estar trabajando con un Hamiltoniano tridiagonal, no es tan complicado obtener una base en la que este sea diagonal. Al obtener los autovalores y autovectores, podemos evaluar cada estado directamente de la solución de la ecuación de Schrödinger. Es importante saber que esos autovalores son los posibles niveles de energía del sistema y los autovectores son funciones de onda. También, la matriz conformada por lo autovectores es la matriz unitaria que tranforma los elementos de una base a otra. Hay que tomar en cuenta que para hacer la operación, debemos tener el estado del sistema en la "base diagonal". Para hacer la transformación, multiplicamos el conjugado hermítico de la matriz de autovectores por el estado en la "base de espines". Con esto listo, se puede evaluar directamente el siguiente estado del sistema. No obstante, el resultado va a estar en la "base diagonal", ya que se calculó en esa base. Solo basta con multiplicar la  base de autovectores por el estado obtenido. Esto debe hacerse para cada paso temporal.

Ya conocemos las metodologías con las que se puede visualizar la dinámica del sistema.

## ¿Qué representa que el estado sea un arreglo de números complejos?

Lo que estamos tratando de observar es el comportamiento de un sistema en una grilla unidimensional. El estado inicial, es con el fermión en el centro de esta. Sin embargo, con el paso del tiempo, hay varios valores de la grilla que toman un valor diferente de 0. Estos valores son números complejos.  Es contraintuitivo que el fermión pueda estar en varios puntos a la vez. Lo que sucede es que cuando empieza a moverse, se comporta como una onda. Esto quiere decir, que no se sabe con certeza su posición exacta. No obstante, sí se puede obtener la probabilidad de cada una de las posiciones. La probabilidad que tiene de estar en un punto de la grilla es igual a la norma al cuadrado del número complejo en su respectiva entrada. Esto hay que aplicarlo en las metodologías, ya que es lo que nos interesa obtener. 

Dependiendo del tiempo en el que se evalúa la dinámica, el fermión puede llegar hasta el final de la grilla. Después de eso, lo que se va a observar es que la onda se refleja en la frontera y se dirige hacia el centro de la grilla de nuevo. En la realidad, esto no pasa, pero en el modelo no existe espacio más allá de la grilla, por eso ocurre de esa forma. 


