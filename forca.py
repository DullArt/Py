import random


def imprime_mensagem_aberta():
    print("**************************")
    print("Bem vindo ao jogo de adivinhação")
    print("**************************")

def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    return palavra_secreta

def iniciar_letras_acertadas(palavras):
    return ["_" for letra in palavras]
    # "_""_""_""_""_""_""

def pede_chute():
    chute = input("Escolha uma letra: ")
    chute = chute.strip().upper()
    return chute

def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
         index += 1

def jogar():

    imprime_mensagem_aberta()
    carregar_palavra_secreta()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = iniciar_letras_acertadas(palavra_secreta)


    enforcou = False
    acertou = False
    erros = 0

    while(not acertou and not enforcou):
            chute = pede_chute()

            if(chute in palavra_secreta):
               marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
            else:
                erros +=1
                print("Erros "+erros)

            enforcou= erros == 6
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo!")



if(__name__=="__main__"):
    jogar()
