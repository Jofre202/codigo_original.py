import matplotlib.pyplot as plt

versiones = ['Original', 'Optimizado']
tiempos = [45.23, 2.14]

plt.figure(figsize=(8,5))

plt.bar(versiones, tiempos, color=['red', 'green'])

plt.title('Comparativa de tiempos')
plt.ylabel('Tiempo (segundos)')

plt.savefig('comparativa_tiempos.png')

plt.show()