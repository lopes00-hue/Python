class Carro:
    def __init__(self,marca, modelo,cor,ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano 

    def acelerar(self):
        print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está acelerando")
   
    def frear(self):
        print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está freando")

# Criando dois objetos diferentes
Carro1 = Carro ("toyota" , "Corolla" , "Azul" , "2012")
carro2 = Carro ("Honda" , "Civic" , "Preto" , "2019") 
carro3 = Carro ("Mercedes" , "g63" , "Branco" , "2025")

# Chamando métodos
Carro1.acelerar() # Usa os atributus do carro1
carro2.acelerar() # Usa os atributus do carro2
carro3.acelerar() # Usa os atributus do carro3

Carro1.frear() # Usa os atributus do carro1
carro2.frear() # Usa os atributus do carro2
carro3.frear() # Usa os atributus do carro3