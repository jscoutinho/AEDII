import time

def merge(esq, di):
    final = []
    i = j = 0

    while i < len(esq) and j < len(di):
        if esq[i] < di[j]:
            final.append(esq[i])
            i+=1
        else:
            final.append(di[j])
            j+=1
    
    final.extend(esq[i:])
    final.extend(di[j:])

    return final

def mergeSort(A):
    if len(A) <= 1:
        return A
    else:
        meio = len(A)//2
        esq = A[:meio]
        di = A[meio:]

        mesq = mergeSort(esq)
        mdir = mergeSort(di)

        return merge(mesq, mdir)



def quickSort(A, inicio, fim):
    if inicio < fim:
        p = particiona(A, inicio, fim)
        quickSort(A, inicio, p - 1)
        quickSort(A, p + 1, fim)

def particiona(A, inicio, fim):
    pivo = A[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if A[j] <= pivo:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[fim] = A[fim], A[i + 1]
    return i + 1



with open("./100.txt", "r") as arquivo:
    linha = arquivo.readline()
    numeros = list(map(int, linha.strip().split(',')))

inicio = time.time()
ordenados = mergeSort(numeros)
fim = time.time()
d = fim - inicio
print(f'Merge Sort - 100 elementos: {d:.6f} segundos')

inicio = time.time()
ordenados = quickSort(numeros,0,len(numeros)-1)
fim = time.time()
d = fim - inicio
print(f'Quick Sort - 100 elementos: {d:.6f} segundos')


# 500.txt
with open("./500.txt", "r") as arquivo:
    linha = arquivo.readline()
    numeros = list(map(int, linha.strip().split(',')))
    
inicio = time.time()
ordenados = mergeSort(numeros)
fim = time.time()
d = fim - inicio
print(f'Merge Sort - 500 elementos: {d:.6f} segundos')

inicio = time.time()
ordenados = quickSort(numeros,0,len(numeros)-1)
fim = time.time()
d = fim - inicio
print(f'Quick Sort - 500 elementos: {d:.6f} segundos')

# 1000.txt
with open("./1000.txt", "r") as arquivo:
    linha = arquivo.readline()
    numeros = list(map(int, linha.strip().split(',')))
    
inicio = time.time()
ordenados = mergeSort(numeros)
fim = time.time()
d = fim - inicio
print(f'Merge Sort - 1000 elementos: {d:.6f} segundos')

inicio = time.time()
ordenados = quickSort(numeros,0,len(numeros)-1)
fim = time.time()
d = fim - inicio
print(f'Quick Sort - 1000 elementos: {d:.6f} segundos')

# 1 milhão
with open("./1000000.txt", "r") as arquivo:
    linha = arquivo.readline()
    numeros = list(map(int, linha.strip().split(',')))
    
inicio = time.time()
ordenados = mergeSort(numeros)
fim = time.time()
d = fim - inicio
print(f'Merge Sort - 1.000.000 elementos: {d:.6f} segundos')

inicio = time.time()
ordenados = quickSort(numeros,0,len(numeros)-1)
fim = time.time()
d = fim - inicio
print(f'Quick Sort - 1.000.000 elementos: {d:.6f} segundos')

# 10 milhões
with open("./10000000.txt", "r") as arquivo:
    linha = arquivo.readline()
    numeros = list(map(int, linha.strip().split(',')))
    
inicio = time.time()
ordenados = mergeSort(numeros)
fim = time.time()
d = fim - inicio
print(f'Merge Sort - 10.000.000 elementos: {d:.6f} segundos')

inicio = time.time()
ordenados = quickSort(numeros,0,len(numeros)-1)
fim = time.time()
d = fim - inicio
print(f'Quick Sort - 10.000.000 elementos: {d:.6f} segundos')
