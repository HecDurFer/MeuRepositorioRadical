import random
import tkinter as tk

#erro: caso o jogador de um input inválido, o programa não faz nada

def jogo_pedra_papel_tesoura(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate!"

    elif (jogador1 == 'pedra' and jogador2 == 'tesoura') or (jogador1 == 'tesoura' and jogador2 == 'papel') or (jogador1 == 'papel' and jogador2 == 'pedra'):
        return "Jogador 1 venceu!"

    elif (jogador2 == 'pedra' and jogador1 == 'tesoura') or (jogador2 == 'tesoura' and jogador1 == 'papel') or (jogador2 == 'papel' and jogador1 == 'pedra'):
        return "Jogador 2 venceu!"

    else:
        return "Jogada inválida!"

def verificar_escolha():
    jogada_jogador1 = entrada.get().lower()
    if jogada_jogador1 in ['pedra', 'papel', 'tesoura']:
        jogada_jogador2 = random.choice(['pedra', 'papel', 'tesoura'])
        resultado = jogo_pedra_papel_tesoura(jogada_jogador1, jogada_jogador2)
        label_resultado.config(text="Jogador 2 escolheu: " + jogada_jogador2 + "\n" + resultado)


# Criando a janela
janela = tk.Tk()
janela.title("Pedra, Papel e Tesoura")

# Rótulo de instrução
label_instrucao = tk.Label(janela, text="Jogador 1, escolha pedra, papel ou tesoura:")
label_instrucao.pack()

# Entrada do jogador 1
entrada = tk.Entry(janela)
entrada.pack()

# Botão para verificar a escolha
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_escolha)
botao_verificar.pack()

# Rótulo do resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Iniciando o loop da janela
janela.mainloop()