def bin(A, x):
    i = 0
    f = len(A)-1

    while i <= f:
        meio = (i+f)//2
        if A[meio] == x:
            return True
        elif A[meio] < x:
            i = meio + 1
        else:
            f = meio -1
    return False

n = int(input("Númeor de Posições: "))
pos = list(map(int,input("Posições: ").split()))
x = int(input("Verificar posição: "))

if bin(pos,x):
    print("Tesouro encontrado!")
else:
    print("Nenhum tesouro nessa posição.")