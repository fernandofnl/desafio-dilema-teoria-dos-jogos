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

#contadores modo de jogo
contador_jogo_simples = 0
contador_olho_por_olho = 0
contador_olho_por_dois_olhos = 0
contador_provador_ingenuo = 0
contador_retalhador_permanente = 0

# contadores dos resultados das partidas
contador_trair_trair = 0
contador_cooperar_trair = 0
contador_trair_cooperar = 0
contador_cooperar_cooperar = 0

numero_partidas = 0
escolheu_trair = 0
escolheu_cooperar = 0


while programa:

    print(menu)
    
    opcao_de_jogo = int(input("Escolha uma opção para jogar: "))

    while validacao:
    
        if  opcao_de_jogo > 5 or opcao_de_jogo < 0:
            print("Opção inválida!")
            opcao_de_jogo = int(input("Escolha uma opção para jogar: "))

        else:
            validacao = False

    if opcao_de_jogo == 1:

        while True:

            print(f"\n==== Jogo Simples ====")
            
            contador_jogo_simples += 1
            escolha_computador = random.randint(1, 2)

            decisao_jogador = int(input("Qual sua decisão? 1. Trair ou 2. Cooperar: "))
            numero_partidas += 1

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

            jogar_novamente = int(input(f"\nVocê deseja jogar novamente? 1. Sim ou 2. Não: "))

            if jogar_novamente == 2:
                break

    elif opcao_de_jogo == 2:

        escolha_computador = random.randint(1, 2)
        
        while True:

            print(f"\n==== Olho por olho ====")
            numero_partidas += 1
            contador_olho_por_dois_olhos += 1
            
            decisao_jogador = int(input("Qual sua decisão? 1. Trair ou 2. Cooperar: "))

            if decisao_jogador == 1 and escolha_computador == 1:

                print(f"\nAmbos os jogadores escolheram trair.")
                escolha_computador = 1
                contador_trair_trair += 1

            elif decisao_jogador == 1 and escolha_computador == 2:

                print(f"\nVocê escolheu trair e o seu parceiro escolheu cooperar.")
                escolha_computador = 1
                contador_trair_cooperar += 1

            elif decisao_jogador == 2 and escolha_computador == 1:

                print(f"\nVocê escolheu cooperar e seu parceiro escolheu trair.")
                escolha_computador = 2
                contador_cooperar_trair += 1

            elif decisao_jogador == 2 and escolha_computador == 2:

                print(f"\nAmbos os jogadores escolheram cooperar.")
                escolha_computador = 2
                contador_cooperar_cooperar += 1

            jogar_novamente = int(input(f"\nVocê deseja jogar novamente? 1. Sim ou 2. Não: "))

            if jogar_novamente == 2:
                break

    elif opcao_de_jogo == 3:

        contador_de_traicao = 0

        while True:

            print(f"\n==== Olho por dois olhos ====")
            numero_partidas += 1
            contador_olho_por_dois_olhos += 1
            escolha_computador = 2

            if contador_de_traicao >= 2:
                escolha_computador = 1

            decisao_jogador = int(input("Qual sua decisão? 1. Trair ou 2. Cooperar: "))

            if decisao_jogador == 1 and escolha_computador == 1:

                print(f"\nAmbos os jogadores escolheram trair.")
                escolha_computador = 1
                contador_trair_trair += 1
                contador_de_traicao += 1

            elif decisao_jogador == 1 and escolha_computador == 2:

                print(f"\nVocê escolheu trair e o seu parceiro escolheu cooperar.")
                escolha_computador = 1
                contador_trair_cooperar += 1
                contador_de_traicao += 1

            elif decisao_jogador == 2 and escolha_computador == 1:

                print(f"\nVocê escolheu cooperar e seu parceiro escolheu trair.")
                escolha_computador = 2
                contador_cooperar_trair += 1
                contador_de_traicao = 0

            elif decisao_jogador == 2 and escolha_computador == 2:

                print(f"\nAmbos os jogadores escolheram cooperar.")
                escolha_computador = 2
                contador_cooperar_cooperar += 1
                contador_de_traicao = 0

            jogar_novamente = int(input(f"\nVocê deseja jogar novamente? 1. Sim ou 2. Não: "))

            if jogar_novamente == 2:
                break
    
    elif opcao_de_jogo == 0:

        programa = False
        relatorio = f"""
==== Relatorio ====

Você jogou {numero_partidas} partidas.

Resultados das partidas:
- Trair x Trair: {((contador_trair_trair * 100) / numero_partidas):.1f}%
- Trair x Cooperar: {((contador_trair_cooperar * 100) / numero_partidas):.1f}%
- Cooperar x Trair: {((contador_trair_trair * 100) / numero_partidas):.1f}%
- Cooperar x Cooperar: {((contador_cooperar_cooperar * 100) / numero_partidas):.1f}%

Você escolheu:
- {escolheu_trair} vezes Trair        -   {(escolheu_trair * 100 / numero_partidas):.1f} das partidas
- {escolheu_cooperar} vezes Cooperar  -   {(escolheu_cooperar * 100 / numero_partidas):.1f} das partidas
"""
        
print(relatorio)
