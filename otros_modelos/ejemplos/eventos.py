import tkinter as tk

def saludar():
  """Muestra un mensaje de saludo."""
  label.config(text="¡Hola! con eventos")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de eventos")

# Crear un botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

# Crear una etiqueta
label = tk.Label(ventana, text="")
label.pack()

# Iniciar el bucle de eventos
ventana.mainloop()