#RA: 1136142        LUÍS FRANKLIN HELMAN MACEDO

#bibliotecas
import os, time , random

#Criando variáveis de ambiente:
    #funcionalidades
def tempo_limpa(segundos):
    time.sleep(segundos)
    os.system("cls")

def limpar_tela():
    os.system("cls")

def tempo(segundos):
    time.sleep(segundos)

    #cores
def verde():
    os.system("color A")

def azul():
    os.system("color B")

def vermelho():
    os.system("color C")

def roxo():
    os.system("color D")

def amarelo():
    os.system("color E")

def branco():
    os.system("color F")

#############################################################################################################################################################################

#jogo da forca:
def jogoDaForca():
    #Boas vindas
    limpar_tela()
    azul()
    print('''
 /$$      /$$           /$$ /$$                                                     /$$                      /$$$$$$            /$$                        
| $$  /$ | $$          | $$| $$                                                    | $$                     /$$__  $$          | $$                        
| $$ /$$$| $$  /$$$$$$ | $$| $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$$$$$    /$$$$$$       | $$  \__/  /$$$$$$ | $$  /$$$$$$  /$$$$$$/$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$      |_  $$_/   /$$__  $$      |  $$$$$$  |____  $$| $$ /$$__  $$| $$_  $$_  $$
| $$$$_  $$$$| $$$$$$$$| $$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$        | $$    | $$  \ $$       \____  $$  /$$$$$$$| $$| $$$$$$$$| $$ \ $$ \ $$
| $$$/ \  $$$| $$_____/| $$| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/        | $$ /$$| $$  | $$       /$$  \ $$ /$$__  $$| $$| $$_____/| $$ | $$ | $$
| $$/   \  $$|  $$$$$$$| $$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$        |  $$$$/|  $$$$$$/      |  $$$$$$/|  $$$$$$$| $$|  $$$$$$$| $$ | $$ | $$
|__/     \__/ \_______/|__/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/         \___/   \______/        \______/  \_______/|__/ \_______/|__/ |__/ |__/
          ''')
    print("Antes de começarmos vamos definir o nome dos jogadores...")
    tempo_limpa(4)

    #Definindo o nome dos jogadores:
    verde()
    print("Bem-vindo à Salém, Desafiante! Escolha o seu nickname: ")
    desafiante = input()
    tempo_limpa(1)
    print("Qual é o nickname do competidor: ")
    competidor = input()
    tempo_limpa(1)
    azul()
    print(f"Certo {desafiante} e {competidor}! Vocês agora vão testar seus instintos e enfrentar um deafio totalmente diferente...")
    tempo_limpa(3)

    #Definirinformações como: palavra-chave, dicas 1,2 e 3
    print("Antes de começarmos, vamos definir combinados essencias para a jogabilidade de vocês.")
    input("Pressione ENTER para continuar...")
    limpar_tela()

    vermelho()
    print(f"Bem-vindo Desafiante {desafiante}!")
    tempo(0.5)
    print(f"Antes de iniciar o jogo é importante definirmos a palavra-chave para o Competidor {competidor} advinhar.")
    tempo(0.5)
    palavra_chave = input("Qual é a palavra-chave do jogo? ").strip().lower()
    tempo(1)
    dicas = []
    dicas.append (input("Insira a dica 1: "))
    dicas.append (input("Insira a dica 2: "))
    dicas.append (input("Insira a dica 3: "))
    tempo_limpa(1)

    #variáveis do jogo
    azul()
    print(f"Seja bem-vindo Competidor {competidor}! Você deve advinhar a palavra-chave secreta para escapar da forca e vencer o jogo...")
    chances = 6
    vermelho()
    print(f"Você tem {chances} chances de erro antes que seja pego pela forca...")
    azul()
    input("Pressione ENTER quando estiver pronto...")

    #looping principal do jogo da forca
    letras_competidor = []
    ganhou = False
    erros = 0

    while True:
        tempo_limpa(2)
        amarelo()
        secreta = ""
        for letra in palavra_chave:
            if letra.lower() in letras_competidor:
                secreta = secreta  + letra
            else:
                secreta = secreta + " * "
        print()
        print(secreta)

        print()
        print(f"Você errou {erros} vezes de {chances} chances")
        print()
        opcao = input("Você quer JOGAR (0) ou PEDIR DICA (1)? ")
        if opcao == "0":
            tentativa = input("Insira a letra: ").strip().lower()
            letras_competidor.append(tentativa)
            if tentativa not in palavra_chave:
                erros = erros + 1 
        elif opcao == "1":
            if len(dicas) > 0:
                print("Dica: ", dicas.pop(0))
                while True:
                    tempo(0.5)
                    tentativa = input("Insira a letra: ").strip().lower()
                    if tentativa not in palavra_chave:
                        erros = erros + 1
                    if len(tentativa) == 1:
                        letras_competidor.append(tentativa)
                        break
            else:
                print("Não tem mais dicas.")
        else:
            print("Inválido. Tente novamente.")
            continue

        if erros > 6:
            tempo_limpa(1.5)
            print(f"Você esgotou as tentativas, vitória do Desafiante {desafiante}!")
            tempo(2)
            break

        if set(palavra_chave) <= set(letras_competidor):
            tempo_limpa(1.5)
            print(f"Parabéns {competidor}. Você ganhou, a palavra-chave secreta era: {palavra_chave}")
            tempo(2)
            ganhou = True
            break

#######################################################################################################################



while True:
    jogoDaForca()
    tempo(3)
    limpar_tela()
    verde()
    print("ÉPICOO!! O que acham de jogar mais uma vez e enfrentar um novo desafio? (s)Sim (n)Não: ")
    resposta = input().strip().lower()
    if resposta != "s":
        print("Obrigado por jogar! Até a próxima.")
        break

