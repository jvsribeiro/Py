print('-$-' * 10)
print('\033[1;34mBanco JR Brasil\033[0;0m')
print('-$-' * 10)

saque = int(input('\033[1;92m Olá, bem-vindo ao Banco saque, qual valor deseja sacar? \033[0;0m'))
total = saque
nota = 50
totalfinal = 0
while True:
    if total >= nota:
        total -= nota
        totalfinal += 1
    else:
        if totalfinal > 0:
            print(f'\033[1;35m	O saque sera feito em  {totalfinal} de R${nota}\033[0;0m ')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota= 5
        elif nota ==5:
            nota = 1
        totalfinal=0
        if total == 0:

                print('\033[1;34m-$-' * 10)
                print('Fim do saque')
                print('-$-' * 10)
                break



