# Crie um módulo chamado manipulacao_strings que
# contenha funções para realizar operações com strings,
# como inverter uma string, contar o número de palavras

# em uma string e verificar se uma string é um
# palíndromo (lê-se igual de trás para frente). Crie
# um programa principal que importe o módulo e use
# essas funções com strings fornecidas pelo usuário.

from funcoes import inverter

while True:
    # print()
    # print('### Manipulando Strings ###')
    # print('1 - Para inverter string')
    # print('2 - Para contar as letras')
    opcoes = input(
        '''
        1 - Para inverter string
        2 - Para contar as letras
        '''
    )
    
    escolha = input('->')
    
    match escolha:
        case 1:
            palavra = input('Digite a palavra que deseja inverter: ')
            print(f'A palavra invertida ficou: {inverter(palavra)}')
    