# Desafio: Dilema do prisioneiro

Problema famoso da Teoria dos Jogos que ilustra o dilema de prisioneiros em tomarem a decisão de trair ou cooperar.

• Trair: significa realizar uma ação onde se busca o maior ganho próprio em prejuízo do outro.
• Cooperar: significa realizar uma ação mediadora que busque trazer compartilhamento de custos e benefícios em uma interação.

1.	Implementar um programa em Python que simule o Dilema do Prisioneiro.

2.	Um será o usuário e o outro é o computador que decidirá sua ação conforme a estratégia selecionada.

3.	Inicialmente o programa deve pedir qual a estratégia a ser utilizada:
a)	Não-Iterado

No jogo simples Não-Iterado – DPNI, cada rodada é independente uma da outra.

b)	Olho por olho

Repete a última escolha do oponente, ou seja, se o jogador 1 trai, o jogador 2 também trai; se jogador 1 coopera; o jogador 2 também coopera. Olho por olho nunca entra em um conflito desnecessário. Na primeira execução, a decisão é aleatória.

c)	Olho por dois olhos

Semelhante a Olho por olho, exceto que o oponente necessita fazer a mesma escolha duas vezes em uma linha antes de haver retaliação, ou seja, jogador 1 coopera enquanto jogador 2 não trair duas ou mais vezes.

d)	Provador Ingênuo

Repete a última escolha do oponente (como em Olho por Olho), mas às vezes trai no lugar de cooperação, ou seja, jogador coopera ou trai de acordo com as ações do jogador, mas trai de forma aleatória.

e)	Retalhador Permanente.

Coopera até o oponente trair e caso isto ocorra sempre escolherá a opção de trair. 

4.	Definida a estratégia, deverá ser perguntado ao usuário se ele trairá ou cooperará. Após a escolha do usuário, o computador seleciona sua resposta conforme a estratégia, apresentando para o usuário o resultado.

5.	Após essa execução, o programa deve perguntar se o usuário quer jogar novamente nessa estratégia ou se ele deseja mudar. Caso ele deseje continuar a estratégia o programa deve solicitar uma nova escolha ao usuário e selecionará uma resposta para o computador ainda conforme essa estratégia.
Caso o usuário queira mudar a estratégia, deverá aparecer novamente a opção de escolher uma estratégia e simular o jogo para essa nova estratégia.

