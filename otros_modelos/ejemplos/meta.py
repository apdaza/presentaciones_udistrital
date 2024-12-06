def crear_clase(nombre, atributos):
  """Crea una clase dinámicamente."""
  cuerpo = {}
  for atributo in atributos:
    cuerpo[atributo] = None
  return type(nombre, (object,), cuerpo)

# Crear una clase "Persona" con atributos "nombre" y "edad"
Persona = crear_clase("Persona", ["nombre", "edad"])

# Crear una instancia de la clase
persona = Persona()
persona.nombre = "Juan"
persona.edad = 30

print(type(persona))
print(persona.nombre)  # Salida: Juan
print(persona.edad)  # Salida: 30