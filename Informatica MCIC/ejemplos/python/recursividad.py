def producto(n, m):
    if m == 1:
        return n
    return n + producto(n, m-1)

def producto_iterativo(n, m):
    valor = 0
    for i in range(m):
        valor += n
    return valor

print(producto(5, 3))
print(producto_iterativo(5, 3))