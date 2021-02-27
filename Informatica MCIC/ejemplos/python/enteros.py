dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
valor = -1
while valor not in range(len(dias)):
    valor = int(input("Ingrese un entero: "))


print(dias[valor])
"""
for i in range(valor):
    print(i)


if valor == 1:
    print("Domingo")
elif valor == 2:
    print("Lunes")
elif valor == 3:
    print("Martes")
else:
    print("No valido")
"""