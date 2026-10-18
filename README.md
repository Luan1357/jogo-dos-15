# Jogo dos 15: Quebra-cabeça deslizante em Python

## Descrição do projeto

Implementação em Python do clássico **quebra-cabeça dos 15**, jogado em um tabuleiro 4x4 com 15 peças numeradas e um espaço vazio. O objetivo é deslizar as peças até restaurar a ordem crescente, com o espaço vazio na última posição.

O tabuleiro inicia resolvido e é **embaralhado aleatoriamente** por um número de movimentos definido pela dificuldade escolhida (fácil: 10, médio: 20, difícil: 30). O embaralhamento é feito apenas com movimentos válidos do espaço vazio, e o algoritmo **evita desfazer o movimento imediatamente anterior**, impedindo que a máquina ande em círculos e desperdice movimentos do embaralhamento.

O controle é feito **via teclado com as teclas WASD**, movendo o espaço vazio nas quatro direções. Movimentos que sairiam dos limites do tabuleiro são ignorados. A cada jogada, o tabuleiro é redesenhado no terminal e comparado com o gabarito resolvido para **detecção de vitória**, exibindo o total de movimentos usados.

O jogo também inclui uma função de **resolução automática** (tecla `R`), que percorre o histórico de movimentos registrados e os desfaz na ordem inversa, animando as peças de volta até a posição resolvida.

## Limitação técnica

**A resolução automática não usa algoritmo de busca (BFS/A\*).** Ela reverte o próprio histórico de movimentos registrado durante a partida, na ordem inversa, ou seja, funciona apenas para tabuleiros embaralhados por esta execução do programa. Não é capaz de resolver um tabuleiro arbitrário informado de fora.

## Como usar

```
python jogo_dos_15.py
```

Controles: `W` `A` `S` `D` para mover, `R` para resolução automática, `Q` para sair.

## Disciplina

Programação Imperativa, PUCPR, 2026

## Tecnologias utilizadas

- Python

## Estrutura do repositório

- `jogo_dos_15.py`: código-fonte do jogo.

## Contexto acadêmico

Projeto desenvolvido por **Luan Alfredo Lugarini**, estudante de Engenharia da Computação na PUCPR.
