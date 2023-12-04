import random

print('Hello, seja bem-vindo ao meu novo joguinho!')
print('Digite um valor aleatorio ate 10, e tente acertar o valor que a maquina ira gerar.')

y = int(input('Digite um numero aleatorio ate 10:'))

def x():
    return random.randrange(1,10)

z = x()

print(z)

if z < y:
    print("o numero aleatorio foi maior que ", z)
elif z == y:
    print("o numero eh igual a ", z)
else:
    print("o numero aleatorio foi menor que ", z)