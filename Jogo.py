from time import sleep
from random import randint


def regras():
    print("*-*-*-* Regras *-*-*-*")
    sleep(0.5)
    print("- Neste jogo o usuario deve advinhar o numero que a maquina escolheu.")
    sleep(0.5)
    print("- O jogador deve informar a quantidade minimo e maxima de numeros")
    sleep(0.5)
    print("- O jogador vai poder informar um numero e a maquina vai informar se o numero passado é maior ou menor que o numero escolhido")
    sleep(0.5)
    print("-Ao acertar o numero, o jogo ira informar a quantidade de chutes feitos")

def jogo():
    contador = 0
    acerto = True
    numero_minimo = int(input("Digite o valor minimo que o jogo pode gerar: "))
    numero_maximo = int(input("Digite o valor maximo que o jogo pode gerar: "))
    numero_random = randint(numero_minimo, numero_maximo)
    while acerto:
        try:
            jogador = int(input("Digite um valor de chute:"))
            sleep(1)
            contador += 1
            if jogador == numero_random:
                print("Acertou!!!!!")
                sleep(1.5)
                print(f'O Jogador precisou de {contador} chutes para acertar o numero {numero_random}')
                break
            elif jogador > numero_random:
                print("O valor do chute é maior que o numero correto")
            elif jogador < numero_random:
                print("O valor informado é menor que o numero correto")
        except ValueError:
            print("Digite apenas numeros!")


while True:
    print('------------- Jogo da advinhação!! -------------')
    print(f'1 - Regras\n'
          f'2 - Iniciar jogo\n'
          f'3 - Encerrar jogo\n')
    sleep(1)
    try:
        escolha = int(input("Selecione: "))
        sleep(1.2)
        if escolha == 1:
            regras()
            continue
        elif escolha == 2:
            jogo()
            continue
        elif escolha == 3:
            print(f'Encerrando...')
            sleep(1)
            break
    except ValueError:
        print("Digite apenas números")
    print("------------------------------------------------")
