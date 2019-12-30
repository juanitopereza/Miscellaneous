import numpy as np
import matplotlib.pyplot as plt

#%%

imagen = np.loadtxt('map_data.txt')
puntos = np.loadtxt('Punto_Nemo.csv', delimiter=',')

#%%
fig, ax = plt.subplots(figsize=(13,13))

ax.imshow(imagen, cmap='plasma')
circulo = plt.Circle((puntos[1],puntos[0]), puntos[2], color='red', Fill=False)
ax.add_artist(circulo)
plt.plot(puntos[1],puntos[0], 'ro', label=u'Punto Nemo')
plt.legend()
plt.title('$Mapa\ Mundi$')

plt.show()
#plt.savefig('PuntoNemo.pdf')
#plt.close()
