# Torre de Hanói
# O desafio consiste em mover todos os discos de uma haste de origem para uma
# haste de destino, utilizando uma haste auxiliar, obedecendo a três regras: (1)
# mover apenas um disco por vez; (2) cada movimento deve transferir o disco do
# topo de uma pilha para o topo de outra; (3) nenhum disco maior pode ser
# colocado sobre um menor.

#função que move um disco do topo de hi para hf
def moverDisco(hi, hf):
    disco = hi.pop(-1)
    hf.append(disco)

#função "hanoi" recursiva
def hanoi(n, o, d, a):
    if n == 1:
        moverDisco(o, d)
    else:
        hanoi(n-1, o, a, d)
        moverDisco(o, d)
        hanoi(n-1, a, d, o)

#Criando as hates 
h1 = []
h2 = []
h3 = []
n = 0
while n < 3:
    n = i = int(input("Digite o número de discos (mínimo 3): "))

    if n < 3:
        print("Número de discos Inválido!")

while i >= 1:
    h1.append(i)
    i-=1

print("h1:")
print(h1)
print("h2:")
print(h2)
print("h3:")
print(h3)

print("===================")

hanoi(n,h1,h3,h2)

print("h1:")
print(h1)
print("h2:")
print(h2)
print("h3:")
print(h3)
