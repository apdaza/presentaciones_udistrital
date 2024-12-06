import shutil
import os

def crear_copia_seguridad(ruta_origen, ruta_destino):
  """Crea una copia de seguridad de un archivo o directorio."""
  try:
    ruta_origen = os.path.abspath(ruta_origen)  # Convertir a ruta absoluta
    ruta_destino = os.path.abspath(ruta_destino)  # Convertir a ruta absoluta
    os.makedirs(ruta_destino, exist_ok=True)
    for elemento in os.listdir(ruta_origen):
      ruta_elemento_origen = os.path.join(ruta_origen, elemento)
      ruta_elemento_destino = os.path.join(ruta_destino, elemento)
      shutil.copy2(ruta_elemento_origen, ruta_elemento_destino)
    print(f"Copia de seguridad creada en: {ruta_destino}")
  except Exception as e:
    print(f"Error al crear la copia de seguridad: {e}")

# Ejemplo de uso, asumiendo que "base" y "copia" están en el mismo directorio que el script
crear_copia_seguridad("base", "copia")