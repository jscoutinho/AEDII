def bin(A, x, i, f):
    if i > f:
        return False
    meio = (i + f) // 2
    if A[meio] == x:
        return True
    elif A[meio] < x:
        return bin(A, x, meio + 1, f)
    else:
        return bin(A, x, i, meio - 1)


n = int(input("Número de posições: "))
pos = list(map(int, input("Posições: ").split()))
x = int(input("Verificar posição: "))

if bin(pos, x, 0, len(pos) - 1):
    print("Tesouro encontrado!")
else:
    print("Nenhum tesouro nessa posição.")