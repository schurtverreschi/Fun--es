numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Escolha a operação (| + | - | * | / |): ").strip()

match operador:
    case "+":
        resultado = numero1 + numero2
        print(resultado)
    case "-":
        resultado = numero1 - numero2
        print(resultado)
    case "*":
        resultado = numero1 * numero2
        print(resultado)
    case "/":
        if numero2 > 0:
            resultado = numero1 / numero2
            print(resultado)
        else:
            print("Erro: Divisão por zero")


# Resolução com funções lambda:

# soma = lambda x, y: x + y
# subtrai = lambda x, y: x - y
# multiplica = lambda x, y: x * y
# divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"

# x = float(input("Digite o primeiro número: "))
# y = float(input("Digite o segundo número: "))

# operacao = input("Escolha a operação (| + | - | * | / |): ")

# if operacao == '+':
#     print(f"O resultado é: {soma(x, y)}")
# elif operacao == '-':
#     print(f"O resultado é: {subtrai(x, y)}")
# elif operacao == '*':
#     print(f"O resultado é: {multiplica(x, y)}")
# elif operacao == '/':
#     print(f"O resultado é: {divide(x, y)}")
# else:
#     print("Operação inválida")


# Faça como eu fiz: calculadora com lambda

# Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

# Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

# Exemplo de entrada:

# Digite o primeiro número: 10
# Digite o segundo número: 5
# Escolha a operação (| + | - | * | / |): +

# Saída esperada:

# O resultado é: 15
