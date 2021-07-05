import time
import os

def limpaTela():
    os.system('cls')


def espaco():
    print('-' *10)

while True:
    print('---Jogo da Tabuada---')
    num = int(input('Digite um número para saber sua tabuada: '))
    espaco()
    print('{} x {:2} = {} '.format(num, 1, num*1))
    print('{} x {:2} = {} '.format(num, 2, num*2))
    print('{} x {:2} = {} '.format(num, 3, num*3))
    print('{} x {:2} = {} '.format(num, 4, num*4))
    print('{} x {:2} = {} '.format(num, 5, num*5))
    print('{} x {:2} = {} '.format(num, 6, num*6))
    print('{} x {:2} = {} '.format(num, 7, num*7))
    print('{} x {:2} = {} '.format(num, 8, num*8))
    print('{} x {:2} = {} '.format(num, 9, num*9))
    print('{} x {:2} = {} '.format(num, 10, num*10))
    espaco()

    pergunta = str(input('Quer Jogar Novamente? (s/n)? '))

    if pergunta == 'n':
        break
    else:
        print('Aguarde... logo o jogo irá reiniciar :)')
        time.sleep(2)
        limpaTela()