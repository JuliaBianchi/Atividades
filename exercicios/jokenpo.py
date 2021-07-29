import time, os
from random import randint
from funcoes import espaco, fala

while True:
    def jogo():
        itens = ('Pedra', 'Papel', 'Tesoura')
        computador = randint(0,2)

        print("Suas opções são: \n[0] PEDRA \n[1] PAPEL \n[2] TESOURA")
        jogador = int(input("Qual é a sua jogada? "))

        if jogador != 0 and jogador != 1 and jogador !=2:
            print("Jogada Inválida :(")
        else:
            fala()
            espaco()
            print("O computador escolheu: {}" .format(itens[computador]))
            print("O jogador escolheu: {}" .format(itens[jogador]))
            espaco()
        if computador == 0:
            if jogador == 0:
                print("EMPATE")
            elif jogador == 1:
                print("JOGADOR VENCEU")
            elif jogador == 2:
                print("COMPUTADOR VENCEU")

        elif computador == 1:
            if jogador == 0:
                print("COMPUTADOR VENCEU")
            elif jogador == 1:
                print("EMPATE")
            elif jogador == 2:
                print("JOGADOR VENCEU")

        elif computador == 2:
            if jogador == 0:
                print("JOGADOR VENCEU")
            elif jogador == 1:
                print("COMPUTADOR VENCEU")
            elif jogador == 2:
                print("EMPATE")
    jogo()
    
    pergunta = str(input('Quer Jogar Novamente? (s/n)? '))
    if pergunta == 'n':
        break
    else:
        print('Aguarde... logo o jogo irá reiniciar :)')
        time.sleep(2)
        os.system('cls')

