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

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))
# definindo ranges que cada quartil terá
sublista1          = range(0,24)
sublista2          = range(25, 49)
sublista3          = range(50, 74)
sublista4          = range(75, 99)

lista_sublista1    = []
lista_sublista2    = []
lista_sublista3    = []
lista_sublista4    = []

valores_randomicos = range(1,100)
repeticoes         = 0
numero_randomicos  = []

# condição para ser positivo e estar entre 0 a 9
if dimensao in range(0,10):
    # laço que popula a lista com valores aleatorios
    for i in range(dimensao):
        numero_randomicos.append(choice(valores_randomicos))
    # laço que verifica quantas vezes 0 a 9 apareceram na lista
    for j in range(0,100):
        repeticoes = numero_randomicos.count(j)
        if repeticoes == 0: 
            continue
        else:
            # se tiver o numero na lista veja em qual quartil ele se encaixa e adicione ele a lista
            match repeticoes:
                case sublista1:
                    lista_sublista1.append(repeticoes)

            print(f'O numero: <{lista_sublista1}> apareceu <{repeticoes}> vezes')
    
    print(f'<{numero_randomicos}>')
else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')