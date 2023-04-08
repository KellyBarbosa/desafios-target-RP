primeiroNumero = 0
segundoNumero = 1
soma = 1
found = False

num = int(input("Informe um número: "))

while primeiroNumero <= num: 
    soma = segundoNumero + primeiroNumero
    primeiroNumero = segundoNumero
    segundoNumero = soma
    if primeiroNumero == num:
        found = True

if found:
    print(f'O número {num} pertence a sequência de Fibonacci.')
else:
    print(f'O número {num} não pertence a sequência de Fibonacci.')    