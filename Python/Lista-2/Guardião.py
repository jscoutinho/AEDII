#O Guardião dos Segmentos
#Você é um Guardião encarregado de proteger um território dividido em segmentos numerados de 1 a N. 
# Em cada rodada, um inimigo aparece em um desses segmentos e você deve descobrir rapidamente onde ele está escondido.
#• O inimigo se move esporadicamente, mas nunca sai do seu segmento atual enquanto você estiver buscando.
#• O território é um vetor oculto A[1…N], e apenas uma posição possui um valor especial 
#• A cada rodada, você pode perguntar: “O inimigo está entre as posições i e j?”
#• Seu objetivo é encontrar a posição exata do inimigo com o menor número de perguntas possível.


import random

N = 10  
A = [0]*N
inimigo = random.randint(0, N-1)  
A[inimigo] = 1


def pergunta(i, j, A):
    for s in range(i,j+1):
        if A[s] == 1:
            return 1
    return 0


def encontrar_inimigo(A, N):
    inicio = 0
    fim = N-1
    perguntas = 0

    while inicio < fim:
        meio = (inicio + fim) // 2
        perguntas += 1
        
        if pergunta(inicio, meio, A):
            fim = meio
        else:
            inicio = meio + 1

    print(f"Posição inimigo: {inicio}")
    print(f"Quantidade de perguntas: {perguntas}")
    return inicio


encontrar_inimigo(A, N)