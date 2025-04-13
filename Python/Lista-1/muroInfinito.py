# MURO INFINITO
# Imagine que você tem um “muro” (ou simplesmente uma faixa linear) com n
# posições numeradas (por exemplo, de 0 a n−1). Você começa em uma posição
# inicial s (qualquer entre 0 e n−1) e deseja encontrar um elemento (ou verificar se ele
# está em alguma posição). Não se sabe se o elemento está para a esquerda ou para
# a direita de s. Entretanto, a restrição é que você só consegue se mover um passo
# por vez para a esquerda ou para a direita.

#Função que alterna entre mover para direita e esquerda "muroInf"

def muroInf(n, s, x, muro):
    if muro[s] == x:
        return True
    
    i = 1
    acabaEsq = acabaDir = False
    e = d = s
    
    while acabaEsq == False or acabaDir == False:
        if i % 2 == 1:
            if acabaDir == False and (d+1) < n:
                d += 1
            else:
                acabaDir = True

            if muro[d] == x:
                return True

        if i % 2 == 0:
            if acabaEsq == False and (e-1) >= 0:
                e -= 1
            else:
                acabaEsq = True

            if muro[e] == x:
                return True
        i+= 1

    return False

#Criando o muro (hard coded)

muro = [13, 47, 58, 12, 20, 4, 56, 9]
s = 2 #posição inicial
n = 8 #tamanho do muro
#x = 12 #elemento que eu quero achar 


print("========================================")
print("Este é o muro pré-criado: ")
print(muro)
print("========================================")
x = int(input("Digite o elemento que irá ser buscado: "))
print(muroInf(n, s, x, muro))