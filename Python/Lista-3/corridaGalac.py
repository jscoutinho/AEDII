def merge(esq, di):
    final = []
    i = j = 0

    while i < len(di) and j < len(esq):
        
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

N = int(input("Número de pilotos: "))
tempos = list(map(int,input("Tempos: ").split()))

temposF = mergeSort(tempos)
print(temposF)