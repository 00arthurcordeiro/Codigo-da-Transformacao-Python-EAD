# Exercício 1 - Operadores Aritméticos

# Pedindo os números ao usuário e convertendo para decimal (float)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

# Exibindo os resultados de forma organizada
print(f"\nResultados para {num1} e {num2}:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da divisão: {resto}")