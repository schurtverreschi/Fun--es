def converter_vendas(texto):
    valores_texto = texto.split()

    if not valores_texto:
        raise ValueError(
            "\nA entrada não pode estar vazia. Digite ao menos um número.\n"
        )

    try:
        return [int(valor) for valor in valores_texto]
    except ValueError:
        raise ValueError(
            "\nEntrada inválida. Digite somente números inteiros separados por espaço.\n"
        )


def calcular_total(valores):
    return sum(valores)


entrada = input("\nDigite os valores das vendas: ")

try:
    lista_vendas = converter_vendas(entrada)
    total = calcular_total(lista_vendas)
    print(f"\nO total de vendas foi: {total}\n")
except ValueError as erro:
    print(erro)


# Faça como eu fiz: calculando o total de vendas

# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

# Exemplo de entrada:

# Digite os valores das vendas: 100 250 300

# Saída esperada:

# O total de vendas foi: 650
