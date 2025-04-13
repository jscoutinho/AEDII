# O mesmo problema dos salários só que em uma solução recursiva


#função soma recursiva "somaR"

def somaR(array, n):
        if n == 1:
                return array[n-1]
        else:
            return array[n-1]+somaR(array,n-1)




#input dos dados

n = int(input("Digite o tamanho da lista: "))
array = []

for i in range(0, n):
        array.append(int(input(f'Digite o salário Número {i+1}: ')))

print(somaR(array, n))