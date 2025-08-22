palavra = "timao    "

acertos = []

erros = 0

while erros <3 and len (acertos) <len(set(palavra)):
    letra=input('Digite uma letra: ')

    if letra in palavra:
        if letra not in acertos:
            acertos.append(letra)
        print("letra correta")
    else:
        erros +=1
        print(f"letra incorreta!Você tem {3-erros}tentativas")

if len(acertos) == len(set(palavra)):
    print("Parabéns!você acertou a palavra!")
else:
    print(f"Fim de jogo! A palavra era {palavra}")