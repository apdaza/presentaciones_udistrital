import time

def registrar_tiempo(func):
  """Decorador para registrar el tiempo de ejecución de una función."""
  def wrapper(*args, **kwargs):
    inicio = time.time()
    resultado = func(*args, **kwargs)
    fin = time.time()
    print(f"Función {func.__name__} tardó {fin - inicio} segundos")
    return resultado
  return wrapper

@registrar_tiempo
def calcular_factorial(n):
  """Calcula el factorial de un número."""
  if n == 0:
    return 1
  else:
    return n * calcular_factorial(n-1)

# Ejemplo de uso
#calcular_factorial(5)
print(calcular_factorial(5))