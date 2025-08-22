import random

numero = random.randint(1,5)
tentativa =0 

while True:

    palpite =int(input("Digite um numero de 1 a 5: "))
    tentativa += 1

    if palpite < numero:
        print ("o número é maior")
    elif palpite > numero:
        print ("o número é menor")
    else:
        print(" você acertou o número" )
    break