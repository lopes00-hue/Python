from exemplo_carro2 import Carro 

class Pessoa:
    def __init__(self,nome,idade,cidade,exemplo_carro2:Carro):
        self.nome = nome 
        self.idade = idade
        self.cidade = cidade
        self.exemplo_carro2 = Carro 

    def apresentar(self):
        print(f"Meu nome é {self.nome} tenho {self.idade} anos e moro {self.cidade}")

pessoa1 = Pessoa ("Felps","20","São Paulo")
pessoa2 = Pessoa ("Albert", "55", "Xique Xique")

pessoa1.apresentar()
pessoa2.apresentar()