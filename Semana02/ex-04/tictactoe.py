# Função para imprimir o tabuleiro
def print_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Função para verificar se alguém ganhou
def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"
    jogadas = 0

    while True:
        print_tabuleiro(tabuleiro)
        print(f"Jogador {jogador}, é a sua vez.")

        linha = int(input("Escolha uma linha (0, 1, 2): ")
        coluna = int(input("Escolha uma coluna (0, 1, 2): ")

        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2 or tabuleiro[linha][coluna] != " ":
            print("Jogada inválida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador):
            print_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            break
        elif jogadas == 9:
            print_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador = "O" if jogador == "X" else "X"

# Iniciar o jogo
jogo_da_velha()
