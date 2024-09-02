def pertence_fibonacci(n):
    # Inicializa os primeiros valores da sequência de Fibonacci
    a, b = 0, 1

    # Continua gerando a sequência até b ser maior ou igual a n
    while b < n:
        a, b = b, a + b
    
    # Verifica se o número informado pertence à sequência
    if b == n or n == 0:
        return True
    else:
        return False

# Entrada do usuário
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")