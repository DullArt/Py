import random

def jogar():
    print("**************************")
    print("Bem vindo ao jogo de adivinhação")
    print("**************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Difina o nível: "))

    if(nivel==1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {} ".format(rodada,total_de_tentativas))

        numero_secreto = 42
        pontos = 1000

        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        acertou = numero_secreto == chute

        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {}!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, o seu chute foi maior que o número secreto")
                print(numero_secreto)
                if(chute>numero_secreto):
                    print("Você errou seu chute {} é maior que o número".format(chute))
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto")
                print(numero_secreto)
                if(chute<numero_secreto):
                    print("Você errou seu chute {} é menor".format(chute))
                pontos_perdidos = abs(numero_secreto-chute)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()
