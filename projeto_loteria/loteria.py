from random import randint
lista = []

valor = int(input("Quantos você gostaria de apostar: "))
for c in range(0, valor):
    numero = randint(1, 60)
    if numero not in lista:
        lista.append(numero)
    else:
        continue

print(f"Os numeros sorteados foram:", end=" ")
for r in lista:
    print(r, end=" ")
