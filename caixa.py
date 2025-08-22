valor = int(input("Digite o valor do saque: "))
notas = [50,20,10,5]

for nota in notas:
    quantidade = valor // nota
    if quantidade >0:
        print(f"{quantidade}nota(5) de R${nota}")
        
        valor -= quantidade * nota 
if valor >0:
    print(f"valor restante de R$ {valor}não pode ser sacado") 