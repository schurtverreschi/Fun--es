def saudacao(hora):
    try:
        hora_num = int(hora)
        if 0 <= hora_num < 12:
            return "Bom dia"
        elif 12 <= hora_num < 18:
            return "Boa tarde"
        elif 18 <= hora_num < 24:
            return "Boa noite"
        else:
            return "Horário não reconhecido"
    except ValueError:
        return "Insira somente números"


hora = input("Digite a hora atual(0-23): ")
print(saudacao(hora))

# Faça como eu fiz: saudação personalizada

# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

#     Se for antes das 12h, exibir "Bom dia";

#     Entre 12h e 18h, exibir "Boa tarde";

#     Após 18h, exibir "Boa noite".

# Exemplo de entrada:

# Digite a hora atual (0-23): 15

# Saída esperada:

# Boa tarde!
