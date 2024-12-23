#Criar a classe Pessoa
class Pessoa:
    
    def __init__(self, nome, idade, cidade):
        self.nome = nome #declarando atributo publico
        self._idade = idade #declarando atributo protegido (pode ser acessado, mas não recomendado)
        self.__cidade = cidade #declarando atributo privado (inacessível e imutável fora da classe)

#Instanciar a classe Pessoa num objeto pessoa
pessoa = Pessoa("Gabriel", 28, "Recife-PE")

#Chamar atributo publico
print(pessoa.nome)

#Chamar atributo protegido
print(pessoa._idade)

#Chamar atributo privado
print(pessoa.__cidade)