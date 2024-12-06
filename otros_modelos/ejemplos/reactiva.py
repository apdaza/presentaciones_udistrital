from rx import operators as ops
from rx import subject

# Crear un sujeto (observable)
observable = subject.Subject()

# Definir una función para procesar los datos
def procesar_datos(x):
  print(f"Procesando dato: {x}")

# Suscribirse al observable y aplicar operadores
observable.pipe(
  ops.map(lambda x: x * 2),  # Multiplicar cada valor por 2
  ops.filter(lambda x: x > 10)  # Filtrar los valores mayores que 10
).subscribe(procesar_datos)

# Emitir valores al observable
observable.on_next(5)
observable.on_next(12)
observable.on_next(7)