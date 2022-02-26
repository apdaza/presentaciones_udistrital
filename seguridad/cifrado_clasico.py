from collections import Counter

def cambio_cifrado(caracter):
    original = ['A','B','C','D','E','F',
                'G','H','I','J','K','L',
                'M','N','O','P','Q','R',
                'S','T','U','V','W','X',
                'Y','Z']

    corrido = ['D','E','F','G','H','I',
            'J','K','L','M','N','O',
            'P','Q','R','S','T','U',
            'V','W','X','Y','Z','A',
            'B','C']
    
    indice = corrido.index(caracter)

    return original[indice]

m = ["HLWWGWHGHBDQOHLGSWW_UHGO","OQLRLDOHU__WLQDDUHRSDOLR","_VQ_F__E_OLHJF__HAVD_XU_"]

matriz = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

m = ""
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        m += matriz[i][j]

counter = Counter(m)
print(counter)
"""
for c in m:
    if c == '_':
        print(' ',end='')
    else:
        print(cambio_cifrado(c), end='')
"""