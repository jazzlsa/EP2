# EP2

Projeto 2 da disciplina de DesSoft.

Regras do jogo:

O jogo consiste no computador escolher um país qualquer, então, o jogador tem 20 tentativas para descobrir qual foi o país escolhido. Além das tentativas, o jogador pode comprar dicas, no mercado de dicas, a fim de descobrir tal país.


Início do jogo:

O computador escolhe um país;
O computador concede 20 tentativas de acertos para o jogador;
O jogador pode tentar um país ou comprar uma dica.


Movimentos possíveis:

A cada jogada, o jogador pode tentar acertar um país ou comprar uma dica;
Ao tentar acertar um país, só será contabilizado a perda de uma tentativa se o país tentado existir e for inédito na lista de tentativas;
A cada tentativa, o computador registra a tentativa de acerto numa lista ordenada de forma crescente pela distância de Haversine, colorindo de forma progressiva as distâncias mais próximas das mais distantes;


Para o cálculo da distância de Haversine no globo terrestre, utilize a aproximação do raio da Terra de 6.371 km.


Caso o jogador opte em comprar uma dica, deve digitar dica no terminal, então, o menu do mercado de dicas deve aparecer para que ele selecione uma dica;


O jogador só pode comprar uma dica se ele tiver tentativas suficientes para isso, caso contrário a compra está impedida.


São dicas:
Cores da bandeira do país;
Letras de sua capital;
População;
Área;
Continente.

Uma vez a dica comprada, ela não pode ser cobrada novamente. Por exemplo: se comprou a área, então, a área não pode ser vendida novamente. Ou, se comprou uma letra de capital, não pode comprar uma letra já comprada anteriormente.


Da vitória:
O jogador ganha se adivinhar o país sorteado pelo computador antes de esgotar suas tentativas.