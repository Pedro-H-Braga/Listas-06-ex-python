'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), cada elemento da lista será uma lista de n elementos. com os
elementos na faixa dos números inteiros entre 0 e 9 (inclusive), gerados aleatoriamente. Imprimir a lista
e calcular e imprimir o determinante dessa “matriz” (usar laço de repetição – NÃO USAR a biblioteca
numpy.py).

https://pt.stackoverflow.com/questions/367434/como-calculo-determinante-de-uma-matriz-quadrada-em-python

'''

from random import choice
from statistics import stdev

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(1,100)
numero_randomicos  = []
desvio_padrao      = 0

# condição para ser positivo e estar entre 0 a 9
if dimensao > 0:
    # laço que popula a lista com valores aleatorios floats
    for i in range(dimensao):
        numero_randomicos.append(choice(valores_randomicos))
