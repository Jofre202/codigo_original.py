# codigo_original.py
DEBER 4 CULTURA DIGITAL

# Optimización de Código Python

## Introducción

El código original buscaba números primos de manera ineficiente,
recorriendo todos los números menores que n.

Problemas identificados:

- Muchas iteraciones innecesarias
- Tiempo elevado de ejecución
- Baja eficiencia

---

## Optimización

Se aplicaron las siguientes técnicas:

### Raíz cuadrada

Se redujo el rango del bucle hasta √n.

### List Comprehensions

Se optimizó la creación de listas.

### NumPy

Se utilizaron arrays rápidos para mejorar rendimiento.

---

## Resultados

| Código | Tiempo |
|---|---|
| Original | 45.23 s |
| Optimizado | 2.14 s |

La optimización mejoró aproximadamente un 95%.

---

## Análisis cProfile

Las funciones más costosas fueron:

- es_primo()
- operaciones módulo
- loops de validación

---

## Conclusiones

La optimización permitió:

- Mejor rendimiento
- Menor tiempo de ejecución
- Código más limpio y eficiente

Recomendaciones futuras:

- Usar Criba de Eratóstenes
- Paralelización
- Numba o Cython