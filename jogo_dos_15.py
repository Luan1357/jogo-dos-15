import random
import time

# Quantidade de movimentos para cada nível
dificuldades = {"1": 10, "2": 20, "3": 30}


# --- FUNÇÕES AUXILIARES ---

def limpar_tela():
    # Limpa a tela do terminal para a animação não ficar descendo
    print('\033[2J\033[H', end='')


def imprimir_tabuleiro(tab):
    # Desenha o tabuleiro na tela
    for linha in tab:
        # Coloca um zero na frente dos números de 1 a 9 para alinhar a tela
        # E substitui o número 0 por um espaço vazio
        linha_formatada = [str(x).zfill(2) if x != 0 else "  " for x in linha]
        print(" | ".join(linha_formatada))
    print("\n")


def obter_inverso(movimento):
    # Devolve a direção contrária do movimento
    inversos = {
        'w': 's', 's': 'w', 'a': 'd', 'd': 'a',
        'Cima': 'Baixo', 'Baixo': 'Cima', 'Esquerda': 'Direita', 'Direita': 'Esquerda'
    }
    return inversos.get(movimento)


def pedir_dificuldade():
    # Pergunta a opção e só deixa o jogo continuar se o jogador digitar 1, 2 ou 3
    escolha = input("\nOpção (1, 2 ou 3): ").strip()
    if escolha in dificuldades:
        return dificuldades[escolha]
    print("Opção inválida! Tente novamente.")
    return pedir_dificuldade()


def calcular_nova_posicao(linha_atual, coluna_atual, direcao):
    # Faz a conta matemática para saber onde o espaço vazio vai parar
    nova_linha = linha_atual
    nova_coluna = coluna_atual

    # Como a linha 0 fica no topo do tabuleiro, ir para 'Cima' significa diminuir a linha
    if direcao in ['w', 'Cima']:
        nova_linha -= 1
    elif direcao in ['s', 'Baixo']:
        nova_linha += 1
    elif direcao in ['a', 'Esquerda']:
        nova_coluna -= 1
    elif direcao in ['d', 'Direita']:
        nova_coluna += 1
    else:
        return None, None  # Se apertar uma tecla errada, não faz nada

    return nova_linha, nova_coluna


# --- CONFIGURAÇÃO INICIAL ---

# Tabuleiro original resolvido (nosso gabarito para saber quando o jogador ganhou)
tabuleiro_resolvido = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

# Cria uma cópia do tabuleiro para jogar sem bagunçar o gabarito original
tabuleiro = [fileira[:] for fileira in tabuleiro_resolvido]

# Guarda onde o número 0 começa (linha 3, coluna 3)
linha_zero, col_zero = 3, 3

# Uma lista vazia que vai guardar todos os movimentos do jogo
historico_total = []

# --- 1. MENU DE DIFICULDADE ---
limpar_tela()
print("=== BEM-VINDO AO JOGO DOS 15 ===")
print("Escolha a dificuldade:")
print("1 - Fácil (10 movimentos)")
print("2 - Médio (20 movimentos)")
print("3 - Difícil (30 movimentos)")

num_embaralhar = pedir_dificuldade()

# --- 2. EMBARALHAMENTO ---
movimentos_feitos = 0
ultimo_sorteio = None

while movimentos_feitos < num_embaralhar:
    opcoes_sorteio = ['Cima', 'Baixo', 'Esquerda', 'Direita']

    # Impede que a máquina desfaça o movimento que ela acabou de fazer
    if ultimo_sorteio:
        inverso_do_ultimo = obter_inverso(ultimo_sorteio)
        if inverso_do_ultimo is not None and inverso_do_ultimo in opcoes_sorteio:
            opcoes_sorteio.remove(inverso_do_ultimo)

    sorteio = random.choice(opcoes_sorteio)
    nova_linha, nova_coluna = calcular_nova_posicao(linha_zero, col_zero, sorteio)

    # Só deixa o movimento acontecer se a peça não for sair do limite do tabuleiro
    if 0 <= nova_linha < 4 and 0 <= nova_coluna < 4:
        # Troca as peças de lugar na matriz
        tabuleiro[linha_zero][col_zero], tabuleiro[nova_linha][nova_coluna] = \
            tabuleiro[nova_linha][nova_coluna], tabuleiro[linha_zero][col_zero]

        # Atualiza onde o zero está agora
        linha_zero = nova_linha
        col_zero = nova_coluna

        # Anota o que a máquina fez no histórico
        historico_total.append(sorteio)
        movimentos_feitos += 1
        ultimo_sorteio = sorteio

        # Mostra a tela embaralhando
        limpar_tela()
        print(f"Embaralhando ({movimentos_feitos}/{num_embaralhar})...")
        imprimir_tabuleiro(tabuleiro)
        time.sleep(0.05)

# --- VARIÁVEIS DO ESTADO DO JOGO ---
movimentos_jogador = 0
jogo_rodando = True

# --- 3. LOOP PRINCIPAL ---
while jogo_rodando:
    limpar_tela()

    print("=== JOGO DOS 15 ===")
    print("WASD: Mover | R: Resolver Auto | Q: Sair")
    print(f"Movimentos feitos: {movimentos_jogador}\n")
    imprimir_tabuleiro(tabuleiro)

    # Checa se o tabuleiro ficou igual ao gabarito original
    if tabuleiro == tabuleiro_resolvido:
        print("=== VOCÊ VENCEU! ===")
        print(f"Resolvido em {movimentos_jogador} movimentos!")
        jogo_rodando = False
        continue

    comando = input("Comando: ").lower().strip()

    if comando == 'q':
        print("Preparando para fechar o jogo...")
        jogo_rodando = False

    elif comando == 'r':
        # Resolve o jogo sozinho se o jogador apertar R
        print("\nIniciando resolução automática...")
        time.sleep(1)

        # Repete isso até esvaziar a lista de histórico
        while historico_total:
            # Pega a última jogada que foi feita na partida
            ultimo_mov = historico_total.pop()
            inverso = obter_inverso(ultimo_mov)

            nova_linha, nova_coluna = calcular_nova_posicao(linha_zero, col_zero, inverso)

            # Desfaz a jogada no tabuleiro
            tabuleiro[linha_zero][col_zero], tabuleiro[nova_linha][nova_coluna] = \
                tabuleiro[nova_linha][nova_coluna], tabuleiro[linha_zero][col_zero]
            linha_zero = nova_linha
            col_zero = nova_coluna

            # Anima a peça voltando para o lugar na tela
            limpar_tela()
            print("Resolvendo automaticamente...")
            print(f"Desfazendo: {ultimo_mov} -> Movendo para: {inverso}")
            imprimir_tabuleiro(tabuleiro)
            time.sleep(0.1)

    else:
        # Pega a direção que o jogador escolheu (WASD)
        nova_linha, nova_coluna = calcular_nova_posicao(linha_zero, col_zero, comando)

        # Ignora se ele apertar uma tecla inválida
        if nova_linha is None:
            continue

            # Só deixa mover se a peça não bater na parede do tabuleiro
        if 0 <= nova_linha < 4 and 0 <= nova_coluna < 4:
            tabuleiro[linha_zero][col_zero], tabuleiro[nova_linha][nova_coluna] = \
                tabuleiro[nova_linha][nova_coluna], tabuleiro[linha_zero][col_zero]
            linha_zero = nova_linha
            col_zero = nova_coluna

            # Anota a jogada do usuário no histórico e conta 1 movimento
            historico_total.append(comando)
            movimentos_jogador += 1

print("Jogo encerrado.")