Valorcompra=float(input('Digite um valor da compra do cliente: '))

if Valorcompra >= 100:   
    desconto=float(Valorcompra - (Valorcompra/10))
    print('Valor da compra com desconto é: ' ,desconto)
else:
    print('Valor da compra sem desconto: ' ,Valorcompra)