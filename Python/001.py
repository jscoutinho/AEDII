# Enunciado do Problema:
# Você recebeu a tarefa de implementar uma função que calcule a soma de todos os
# salários contidos em um array de tamanho n. Cada elemento do array representa o
# salário de um funcionário. Sua função deve receber esse array de salários e retornar
# (ou imprimir) o valor total da soma de todos eles.
# Requisitos:
# • A função deve aceitar um array de inteiros que representam os salários.
# • A função deve retornar (ou imprimir) a soma de todos os valores presentes
# no array.
# • Caso o array esteja vazio, a função deve retornar (ou imprimir) zero.
# Exemplo de entrada/saída:
# • Entrada: [2000, 1500, 4000, 1200]
# • Saída: 8700 


#função iterativa "soma"

def soma(array, n):

    if array == []:
        return 0
    
    somaA = 0

    for i in range(0, n):
        somaA += array[i]

    return somaA


#input dos dados

n = int(input("Digite o tamanho da lista: "))
array = []

for i in range(0, n):
        array.append(int(input(f'Digite o salário Número {i+1}: ')))

print(soma(array, n))