print(' \033[;1m \033[1;07m Software De media escolar \033[0;0m')
name = input('\033[1;m \033[1;93m Digite o nome ')

materia= str(input('Nome de disciplina '))

nota = float(input('Digite nota da prova '))

nota2 = float(input('Digite a nota trabalho prático '))

nota3 = float(input('Digite a nota do projeto final '))

media = ((nota + nota2 + nota3) / 3 )

print(f' \033[1;33m A disciplina é {materia} as notas em análises são {nota}, {nota2} e {nota3} a média final é {media:.3}')
if media >= 7:
    print(f'\033[1;34m Parabêns você foi aprovado!! sua média é {media:.3} ')
else:
    print(f'\033[1;91m Infelizmente você nâo atingiu a média! sua média é {media:.3}, ou seja infereior a 7')



