#Classe base (classe pai)
class Pessoa:
    #metodo constructor
    def __init__(self, nome, cidade):
        self.nome = nome #atributo publico
        self.cidade = cidade #atributo publico
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu moro em {self.cidade}.")
        
#Classe derivada Funcionário (classe filha)
class Funcionario(Pessoa):
    def __init__(self, nome, cidade, cargo, salario):
        super().__init__(nome, cidade) #chamar metodo constructor da classe pai
        self.cargo = cargo #adicionando atributo publico específico para a classe
        self.salario = salario #adicionando atributo publico específico para a classe
            
    def apresentar_funcionario(self):
        self.apresentar()
        print(f"Eu trabalho como {self.cargo} e meu salário é de {self.salario:.2f}.")
        
#Classe derivada Cliente (classe filha)
class Client(Pessoa):
    def __init__(self, nome, cidade, idade):
        super().__init__(nome, cidade) #chamar metodo constructor da classe pai
        self.idade = idade #adicionando atributo publico específico para a classe
    
    def apresentar_cliente(self):
        self.apresentar()
        print(f"Eu tenho {self.idade} anos e sou um cliente.")
    
#Criar o objeto da classe pessoa
pessoa = Pessoa("Gabriel", "Jaboatão dos Guararapes")
pessoa.apresentar()
funcionario = Funcionario("Rafael", "Recife", "Desenvolvedor", 5000)
funcionario.apresentar_funcionario()
cliente = Client("Nayara", "Caruaru", 26)
cliente.apresentar_cliente()