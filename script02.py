'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99
(inclusive), gerados aleatoriamente. Após gerar a lista, determinar as quantidades de elementos que
estão no primeiro quartil (valores entre 0 e 24), no segundo quartil (entre 25 e 49), no terceiro quartil
(entre 50 e 74) e no quarto quartil (entre 75 e 99).

preencher uma lista com valores aleatorios de 0 a 99 e dividir essa lista em 4 sublistas que vao de:
1° sublista: range(0,24)
2° sublista: range(25, 49)
3° sublista: range(50, 74)
4° sublista: range(75, 99)
'''
from random import choice

dimensao = int(input('Informe o numero de elementos da lista: '))
valores = range(1,100)
lista = []

if dimensao > 0:
    for i in range(dimensao):
        lista.append(choice(valores))
        
print(lista)