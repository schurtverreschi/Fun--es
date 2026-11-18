def converter_tipo(lista):
    nova_lista = []

    for item in lista:
        nova_lista.append(int(item))

    return nova_lista


def verificar_conversao(lista):
    for item in lista:
        if type(item) is not int:
            return "\nConversão falhou !\n"

        return "\nTodos os números foram convertidos corretamente!\n"


telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

print(verificar_conversao(converter_tipo(telefones)))

# Faça como eu fiz: conversor de tipos

# Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:

# Exemplo de entrada:

# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

# Saida esperada:

# Todos os números foram convertidos corretamente!
