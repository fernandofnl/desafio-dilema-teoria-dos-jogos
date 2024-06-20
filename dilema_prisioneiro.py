import random

menu = f"""
==== Dilme do Prisioneiro ====

--- Bem-vindo ao jogo ---
Escolha uma opção de jogo:

[1] Jogo simples
[2] Olho por olho
[3] Olho por dois olhos
[4] Provador Ingênuo
[5] Retalhador Permanente
[0] Sair \n"""

programa = True
validacao = True
repetir_partida = True
contador_trair_trair = 0
contador_cooperar_trair = 0
contador_trair_cooperar = 0
contador_cooperar_cooperar = 0
numero_partidas = 1

resultado = f"""
==== Resultados ====

Você jogou {numero_partidas} partidas.

Quantidade de vezes:
- Trair x Trair: {(contador_trair_trair * 100) / numero_partidas}%
- Trair x Cooperar: {(contador_trair_cooperar * 100) / numero_partidas}%
- Cooperar x Trair: {(contador_trair_trair * 100) / numero_partidas}%
- Cooperar x Cooperar: {(contador_cooperar_cooperar * 100) / numero_partidas}%

"""

while programa:

    print(menu)
    opcao_de_jogo = int(input("Escolha uma opção para jogar: "))

    while validacao:
        
        if  opcao_de_jogo > 5 or opcao_de_jogo < 0:
            print("Opção inválida!")

        else:
            validacao = False

    if opcao_de_jogo == 1:

        while True:

            print(f"\n==== Jogo Simples ====")
            numero_partidas += 1
            escolha_computador = random.randint(1, 2)

            decisao_jogador = int(input("Qual sua decisão? 1. Trair ou 2. Cooperar: "))

            if decisao_jogador == 1 and escolha_computador == 1:

                print(f"\nAmbos os jogadores escolheram trair.")
                contador_trair_trair += 1

            elif decisao_jogador == 1 and escolha_computador == 2:

                print(f"\nVocê escolheu trair e o seu parceiro escolheu cooperar.")
                contador_trair_cooperar += 1

            elif decisao_jogador == 2 and escolha_computador == 1:

                print(f"\nVocê escolheu cooperar e seu parceiro escolheu trair.")
                contador_cooperar_trair += 1

            elif decisao_jogador == 2 and escolha_computador == 2:

                print(f"\nAmbos os jogadores escolheram cooperar.")
                contador_cooperar_cooperar += 1

            jogar_novamente = int(input("Você deseja jogar novamente? 1. Sim ou 2. Não: "))

            if jogar_novamente == 2:
                break


    elif opcao_de_jogo == 0:

        programa = False
