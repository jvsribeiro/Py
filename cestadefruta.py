fruit = ['uva']

while True:
    print('Você deseja adicionar uma furta? ')
    chose = (input('adicionar/remover'))
    if chose.lower() == 'adicionar':
        print('Adicione sua fruta')
        new=(input('Sua fruta'))
        fruit.append(f'{new}')
        print(f'Essas são suas frutas:{fruit}')
    if chose.lower() == 'remover':
        print(f'remova sua fruta,essas são as que estão disponiveis{fruit}')
        delet=(input('remova sua fruta'))
        fruit.remove(f'{delet}')
        print(f'essas são as atuais {fruit}')