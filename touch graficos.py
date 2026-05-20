import matplotlib.pyplot as plt

versiones = ['Original', 'Optimizado']
tiempos = [45.23, 2.14]

plt.figure(figsize=(8,5))

plt.bar(versiones, tiempos, color=['red', 'green'])

plt.title('Comparativa de tiempos')
plt.ylabel('Tiempo en segundos')

plt.savefig('comparativa_tiempos.png')

plt.show()

plt.figure(figsize=(8,5))

plt.hist(tiempos, bins=5, color='blue', edgecolor='black')

plt.title('Distribución de tiempos')

plt.savefig('distribucion_tiempos.png')

plt.show()