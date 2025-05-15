def exp(base, expoente):
    if expoente == 0:
        return 1
    elif expoente % 2 == 0:
        meio = exp(base, expoente // 2)
        return meio * meio
    else:
        return base * exp(base, expoente - 1)
    
poderB = int(input("Poder base: "))
nivel = int(input("Nível: "))

danoTotal = exp(poderB, nivel)

print(danoTotal)