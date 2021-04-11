# 01/03/2021 jogo da forca da Alura (curso python parte 02)
import random


def jogar():
    imprime_mensagem_inicial()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pede_chute()
        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            print(letras_acertadas)
        else:
            erros += 1
            letras_faltando = (letras_acertadas.count('_'))
            print("Você errou a letra, ainda faltam acertar {} letras".format(letras_faltando))
            desenha_forca(erros)
            print(letras_acertadas)
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    if acertou:
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)


# ---- funções utilizadas no código ----
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1  # o mesmo que "index = index + 1"


# função que pede um chute de uma letra para o usuário
def pede_chute():
    # .strip(): remove espaços em branco antes e depois da string
    # .upper(): upper case
    chute = input("Digite um letra: ").strip().upper()
    return chute


# função para iniciar a lista de letras acertadas com o caracter "_"
def inicializa_letras_acertadas(palavra):
    letras_acertadas = ["_" for letra in palavra]
    return letras_acertadas


# função que que lê um arquivo de texto externo, carrega uma lista de palavras,
# e retorna uma palavra de forma randomica como "palavra secreta"
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero_indice = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_indice].upper()
    return palavra_secreta


def imprime_mensagem_vencedor(palavra_secreta):
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\ \:      /-.   ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \ \::.    /     ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("Parabén você acertou a palavra secreta: " + palavra_secreta)


def imprime_mensagem_perdedor(palavra_secreta):
    print("  _______   ")
    print(" /       \  ")
    print("|  () ()  | ")
    print(" \   ^   /  ")
    print("   |||||   ")
    print("   |||||   ")
    print("Você enforcou, a palavra secreta era: " + palavra_secreta)


# função que imprime tela de apresentação inicial do jogo da forca
def imprime_mensagem_inicial():
    print("*******************************")
    print("""**BEM VINDO AO JOGO DA FORCA***
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========""")
    print("*******************************")


def desenha_forca(erros):
    print(" +---+")
    print(" |   |")

    if(erros == 1):
        print (" O   |")
        print ("     |")
        print ("     |")

    if(erros == 2):
        print (" O   |")
        print ("/    |")
        print ("     |")

    if(erros == 3):
        print (" O   |")
        print ("/|   |")
        print ("     |")

    if(erros == 4):
        print (" O   |")
        print ("/|\  |")
        print ("     |")

    if(erros == 5):
        print (" O   |")
        print ("/|\  |")
        print ("/    |")

    if(erros == 6):
        print (" O   |")
        print ("/|\  |")
        print ("/ \  |")

    print("     |")
    print("=========")


if __name__ == "__main__":
    jogar()
