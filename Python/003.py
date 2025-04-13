#O mesmo problema dos exercícios anteriores, agora considerando a soma 2 a 2.


#função que soma com um iterador vindo do começo e outro do fim. "soma2"

def soma2(array, n):
    i = 0
    j = n -1
    soma = 0

    while i <= j:
          soma += array[i]+array[j]
          i+= 1
          j-= 1

    return soma

#input dos dados

n = int(input("Digite o tamanho da lista: "))
array = []

for i in range(0, n):
        array.append(int(input(f'Digite o salário Número {i+1}: ')))

print(soma2(array, n))