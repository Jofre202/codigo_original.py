import time
import math
import numpy as np

inicio = time.time()

def es_primo(n):

    if n < 2:
        return False

    limite = int(math.sqrt(n)) + 1

    for i in range(2, limite):
        if n % i == 0:
            return False

    return True

numeros = np.arange(2, 100001)

primos = [n for n in numeros if es_primo(n)]

fin = time.time()

print(f"Cantidad de números primos: {len(primos)}")
print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")