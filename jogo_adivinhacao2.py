import random

numero = random.randint (1,5)

Tentativa = 0

while Tentativa <5:
    palpite = int(input("Digite o seu palpite 1 até o 5: "))
    Tentativa += 1

    if palpite == numero:
        print("Você acertou o número!")
        break
   
    elif palpite < numero: 
        print("O número é menor")

    else:
        print("O número é Maior")

if palpite !=numero:
        print(f"Fim do jogo!O número era {numero}")