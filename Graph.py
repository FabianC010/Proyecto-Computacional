import matplotlib.pyplot as plt
import Diag as dg
import calculo_norma as cn


#Figura compuesta por todos los estados quanticos de RK4
fig, axs = plt.subplots(1,dg.psi.size, figsize=(500, 40), sharey=True)

for i in range(dg.psi.size):
  axs[i].plot(dg.times, cn.norma_cuadrada(dg.stateQuant0[:,i]))
  for spine in axs[i].spines.values():
        spine.set_visible(False)

plt.savefig("Compound.pdf")
plt.show()

#Cada estado cuantico individual de RK4
import matplotlib.pyplot as plt
for i in range(dg.psi.size):
  plt.plot(dg.times, cn.norma_cuadrada(dg.stateQuant0[:,i]))
  plt.title(f'State {i}')
  plt.xlabel('Tiempo')
  plt.ylabel('Probabilidad')
  plt.xlim(0, 10)
  plt.ylim(0, 1)
  plt.grid(True)
  plt.savefig(f'state_{i}.png')