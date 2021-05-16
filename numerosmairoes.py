try:
    print('\033[1;94m Mostrando o maior número')

    a = int(input(" \033[1;33m digite o primeiro numero: "))
    b = int(input(" \033[1;33m digite o sugundo numero: "))
    c = int(input(" \033[1;33m digite o terceiro numero: "))

    if a > b and a > c:
        print(f' \033[0;0m O maior número é {a}')
    elif  b > c and b > a:
        print(f'O maior número é {b}')
    elif c > a and c > b:
        print(f'Seu maior número é {c}')

    elif a == b == c:
        print('todos número são iguais')

    elif a == b:
        print(f'o primeiro número é igual ao segundo e eles são os maiores ou seja {a}')

    elif a == c:
        print(f' o primeiro número e o terceiro são iguais, e eles são maiores ou seja o maior é {a}')
    elif b == c:
        print(f'o segundo e terceiro numero são iguais ou seja eles são os maiores, ou seja o maior é {c}')
except ValueError:

    print(' \033[1;34a Digite apenas números!')
















