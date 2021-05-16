try:
    print('Bem- vindo ao banco Campo Salles- Bebedouro SP')
    print(' \033[1;34m Softwere para aprovação de emprestimo')

    valorcasa = float(input(' \033[;7m Digite o valor da casa: '))
    salario = float(input('Digite o valor de sua renda mensal: '))
    meses = int(input('Qual é o período em meses que será pago o emprestimo: '))

    if ((valorcasa / meses ) > (0.70 * salario)):
        print('\033[0;0m \033[1;91m RECUSADO! \033[1;34m Infelizmente seu emprestimo não foi aprovado')
    else:
        print('\033[0;0m \033[1;32m APROVADO! \033[1;34m Seu imprestimo foi aprovado! proucure um consutor mais proximo para realizar o emprestimo!')
except ValueError:
    print("\033[0;0m \033[1;36m Digite apenas números!")








