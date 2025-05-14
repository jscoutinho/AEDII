
# Contando Inversões em um Vetor
#
# Dado um vetor de números inteiros distintos A=[a1,a2,...,an], uma inversão é um
# par de índices (i,j) tal que i<j e ai>aj .
# Implemente um algoritmo eficiente para contar o número total de inversões no
# vetor utilizando a técnica de divisão e conquista. O algoritmo deve ter
# complexidade no máximo O(nlogn).
# Exemplo de entrada: A = [2, 4, 1, 3, 5]
# Saída esperada: 3

def merge(esq, di):
    final = []
    i = j = 0
    c = 0

    while i < len(esq) and j < len(di):  
        if esq[i] <= di[j]:
            final.append(esq[i])
            i += 1
        else:
            final.append(di[j])
            j += 1
            c += len(esq) - i  

    final.extend(esq[i:])
    final.extend(di[j:])
    return final, c

def mergeSort(A):
    if len(A) <= 1:
        return A, 0

    meio = len(A) // 2
    esq = A[:meio]
    di = A[meio:]

    mesq, c1 = mergeSort(esq)
    mdir, c2 = mergeSort(di)

    merged, c3 = merge(mesq, mdir)

    return merged, c1 + c2 + c3

A = [2, 4, 1, 3, 5]
o, c = mergeSort(A)
print(c) 
