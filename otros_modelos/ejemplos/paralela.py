import threading

def sumar_elementos(lista, inicio, fin, resultado):
  """Suma los elementos de una lista en un rango dado."""
  suma = 0
  for i in range(inicio, fin):
    suma += lista[i]
  resultado.append(suma)

# Lista de números
numeros = list(range(1, 1001))

# Dividir la lista en 4 partes
n = len(numeros)
hilos = []
resultados = []
for i in range(4):
  inicio = i * (n // 4)
  fin = (i + 1) * (n // 4) if i < 3 else n
  hilo = threading.Thread(target=sumar_elementos, args=(numeros, inicio, fin, resultados))
  hilos.append(hilo)
  hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
  hilo.join()

# Sumar los resultados parciales
suma_total = sum(resultados)
print(f"La suma total es: {suma_total}")