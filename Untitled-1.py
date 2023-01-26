lista = [11, 11, 15, 12, 13, 9, 4, 1, 2, 1, 11, 15, 41, 42, 40]
ordenado = []
print(lista)
for numero in lista:
    for chave, valor in enumerate(ordenado):
        if numero < valor:
            ordenado.insert(chave, numero)
            break
    else:
        ordenado.append(numero)
        
print(ordenado)