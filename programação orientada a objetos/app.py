#Definir a classe Pessoa
class Pessoa:
    
    #Metodo inicializador da classe
    def __init__(self, nome, idade): #Passando parâmetros para a classe pessoa
        self.nome = nome #atributo nome
        self.idade = idade #atributo idade
        
    #Metodo para mostrar dados da pessoa
    def mostrar_dados(self):
        print(f"Olá, sou {self.nome}, e tenho {self.idade} anos")

#Instanciar a classe Pessoa em um objeto
pessoa = Pessoa("Gabriel", 28)
print(pessoa)

#Chamar o metodo mostrar dados
pessoa.mostrar_dados()