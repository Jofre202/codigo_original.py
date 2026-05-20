import time

inicio = time.time()

primos = []

for n in range(2, 100001):
    es_primo = True

    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(n)

fin = time.time()

print(f"Cantidad de números primos: {len(primos)}")
print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")