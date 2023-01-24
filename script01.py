'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 9
(inclusive), gerados aleatoriamente. Determinar as quantidades para cada número que foi gerado.

# utilizar a RANDOM.PY
'''
from random import choice

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(1,10)
lista = []
# condição para ser positivo e estar entre 0 a 9
if dimensao in range(0,10):
    for i in range(dimensao):
        lista.append(choice(valores_randomicos))
    print(lista)
else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')