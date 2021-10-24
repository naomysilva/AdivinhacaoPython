import random

total_de_tentativas = 3
rodada = 1
numero_secreto = random.randrange(1,101)

for rodada in range(0, total_de_tentativas):

    print("Tentativa {} de {}".format(rodada + 1, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
  
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue 


    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")