import random
import time

print("Simulador de Tempo de Reação")
print("Pressione enter assim que o 'SINAL' aparecer.")
print("-----")
input("Pressione enter para começar...")
print("-----")
time.sleep(random.randint(1, 5))  # Gera um atraso aleatório entre 1 e 5 segundos
print("SINAL!")
start_time = time.time()
input()  # Aguarda o usuário pressionar enter
end_time = time.time()
reaction_time = end_time - start_time

#solução: verificar se o tempo de reação é menor que 0.00 segundos.

if reaction_time < 0.01:
    print("Botão pressionado antes do sinal ser dado!")
else:
    print("Seu tempo de reação foi de {:.2f} segundos.".format(reaction_time))