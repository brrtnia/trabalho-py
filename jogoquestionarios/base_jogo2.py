from io import FileIO
from os import execl
import sys
import os
from random import randint


def saudar_usuário():
    print(
        "Bem vindo ao jogo adivinhe o número.\n"
        "Acabei de pensar em um número entre 1 e 100. "
        "Tente descobrir esse número.\n"
        "Digite sair para parar de jogar.\n",


    )


def checar_se_usuário_quer_sair(palpite):
    if palpite.strip().lower() == "sair":
        print("Obrigado por jogar. Até a próxima!")
        sys.exit()


def transformar_palpite_em_número(palpite):
    try:
        palpite = int(palpite)
        return palpite
    except ValueError:
        return None


def checar_palpite_correto(palpite, número_aleatório):
    if palpite > número_aleatório:
        print("Muito alto! Eu pensei em um número menor.\n")
    elif palpite < número_aleatório:
        print("Muito baixo! Eu pensei em um número maior.\n")
    else:
        print("Parabéns! Você acertou!\n")
        return True
    return False


def checar_derrota(tentativas,  jogadas, número_aleatório, palpite):
    if palpite != número_aleatório:
        if jogadas == tentativas:
            print("Você perdeu todas as tentativas, tente novamente")
            return True
    return False


def novo_jogo_ou_sair():
    jogar_novamente = input("Jogar novamente? ")

    if jogar_novamente.strip().lower() in ["s", "si", "sim"]:

        return True

    print("Até a próxima!")
    sys.exit()


def saudar_usuário_novo_jogo():
    print(
        "Legal! Acabei de pensar em outro número entre 1 e 100.\n"
        "Tente adivinhar, ou digite sair para finalizar o jogo.\n"
    )


def restart_program():
    python = sys.executable
    sys.stdout.flush()
    os.execl(python, python, * sys.argv)


def adivinhe_o_número():
    saudar_usuário()
    número_aleatório = randint(1, 100)
    jogadas = 0
    print("Escolha um nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        tentativas = 10
    if nivel == 2:
        tentativas = 6
    if nivel == 3:
        tentativas = 3

    while True:
        palpite = input("Digite um número entre 1 e 100: ")
        checar_se_usuário_quer_sair(palpite)

        palpite = transformar_palpite_em_número(palpite)
        if palpite is None:
            print("Erro: Você deve digitar um número! Tente novamente.\n")
            continue

        if 1 <= palpite <= 100:
            palpite_correto = checar_palpite_correto(palpite, número_aleatório)
            jogadas += 1
            derrota = checar_derrota(
                tentativas, jogadas, número_aleatório, palpite)
        else:
            jogadas += 1
            print("Erro: O número deve estar entre 1 e 100! Tente novamente.\n")

            continue

        if derrota:
            sys.exit()

        if palpite_correto:
            novo_jogo_ou_sair()

            saudar_usuário_novo_jogo()

            número_aleatório = randint(1, 100)


if __name__ == "__main__":
    adivinhe_o_número()
