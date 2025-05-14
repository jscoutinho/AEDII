A = [4, 5, 6, 8, 1, 3, 2, 5, 343, 21, 32, 13]

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

mergeSort(A)