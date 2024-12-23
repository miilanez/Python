#Criar a classe Pessoa
class Pessoa:
    def __init__(self, nome):
        self.nome = nome #declarando atributo publico
        self._idade = 27 #declarando atributo protegido (pode ser acessado, mas não recomendado)
        self.__cidade = "Não informada" #declarando atributo privado (inacessível e imutável fora da classe)

    #Getter para atributo idade
    def get_idade(self):
        return self._idade
    
    #Setter para atributo idade
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            print("Idade não pode ser negativa")
            
    #Getter para atributo cidade
    def get_cidade(self):
        return self.__cidade
    
    #Setter para atributo cidade
    def set_cidade(self, nova_cidade):
        self.__cidade = nova_cidade
       
    
#Instanciar a classe Pessoa num objeto pessoa
pessoa = Pessoa("Gabriel")

#Chamar atributo publico
print("Nome: ", pessoa.nome)

#Acessar e modificar o atirbuto protegido
print("Idade atual: ", pessoa.get_idade())
pessoa.set_idade(28)
print("Nova Idade: ", pessoa.get_idade())

#Acessar atributo cidade
print("Cidade Atual: ", pessoa.get_cidade())
pessoa.set_cidade("Caruaru")
print("Nova cidade: ", pessoa.get_cidade())