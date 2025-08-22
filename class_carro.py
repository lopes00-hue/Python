#class = palavra chave no python para definir uma classe

#carro = nome que damos á classe. Por convenção começa com letra se for nome composto, usamos camel case ex: minha casa
class Carro:
    #def =  palavra chave que define uma função função ou métado no Python  
    '''__initi__ = método contrutor da classe.Ele é chamado automaticamente quando criamos a classe com um novo objeto. serve para inicializar atributos do objeto.'''
    #self = Uma referéncia ao próprio objeto que está sendo criado
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"O carro {self.marca} {self.modelo} está acelerando")


# Criando dois objetos diferentes
carro1 = Carro ("toyota" , "Corolla")
carro2 = Carro ("Honda" , "Civic")
carro3 = Carro ("Tesla" , "Cybertruck")

# Chamando métodos
carro1.acelerar() # Usa os atributus do carro1
carro2.acelerar() # Usa os atributus do carro2
carro3.acelerar() # Usa os atributus do carro3