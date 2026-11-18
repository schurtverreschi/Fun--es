from datetime import date, datetime


def calcular_idade(nascimento_str):
    # 1. Converte o texto "DD/MM/AAAA" para um objeto de data real
    nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y").date()
    hoje = date.today()

    # 2. Subtrai os anos e ajusta caso a pessoa ainda não tenha feito aniversário este ano
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    return idade


nascimento = input("Digite seu ano de nascimento [DD/MM/AAAA]: ")
idade = calcular_idade(nascimento)
print(f"\nVocê tem {idade} anos.\n")

# Faça como eu fiz: calculando a idade

# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

# Exemplo de entrada:

# Digite o ano de nascimento: 2005

# Digite o ano atual: 2025

# Saída esperada:

# A idade é 20 anos.
