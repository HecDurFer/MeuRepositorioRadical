import time
import tkinter as tk

#problema: quando inicia a contagem apertando "Enter" e aperta "Parar" antes de terminar, aparece no lugar da contagem "UnboundLocalError"
#isso acontece pois tenta acessar a variável "cronometro_executando" antes de atribuir um valor a ela.

def cronometro(segundos):
    for i in range(segundos, 0, -1):
        if not cronometro_executando[0]:
            return
        label_tempo["text"] = f"Tempo restante: {i} segundos"
        janela.update()
        time.sleep(1)
    label_tempo["text"] = "Tempo esgotado!"


def iniciar_cronometro(event=None):
    segundos = int(entry_segundos.get())
    cronometro_executando[0] = True
    entry_segundos.configure(state="disabled")
    btn_iniciar.configure(state="disabled")
    btn_parar.configure(state="normal")
    cronometro(segundos)

def parar_cronometro():
    cronometro_executando[0] = False
    entry_segundos.configure(state="normal")
    btn_iniciar.configure(state="normal")
    btn_parar.configure(state="disabled")

cronometro_executando = [False]

janela = tk.Tk()
janela.title("Cronômetro")

label_instrucao = tk.Label(janela, text="Digite a quantidade de segundos:")
label_instrucao.pack()

entry_segundos = tk.Entry(janela)
entry_segundos.pack()
entry_segundos.bind('<Return>', iniciar_cronometro)

btn_iniciar = tk.Button(janela, text="Iniciar", command=iniciar_cronometro)
btn_iniciar.pack()

btn_parar = tk.Button(janela, text="Parar", command=parar_cronometro, state="disabled")
btn_parar.pack()

label_tempo = tk.Label(janela, text="")
label_tempo.pack()

janela.mainloop()
