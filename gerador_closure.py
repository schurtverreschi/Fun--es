def aplicar_desconto(porcentagem):
    def valor(valor):
        return valor - (valor * porcentagem / 100)

    return valor


porcentagem = int(input("Digite a porcentagem de desconto: "))
valor = float(input("Digite o valor da compra: "))

desconto = aplicar_desconto(porcentagem)

print(f"Preço final com desconto: R$ {desconto(valor):.2f}")


# Faça como eu fiz: gerador de funções personalizadas

# Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.

# Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

# Exemplo de entrada:

# Digite a porcentagem de desconto: 10
# Digite o valor da compra: 200

# Saída esperada:

# Preço final com desconto: 180.0
