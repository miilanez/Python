#Estrutura Básica de uma Função

def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()

# Função com Parâmetros

def saudacao_com_nome(nome):
    print(f"Olá, {nome}!")
    #f indica que quero formatar a string

saudacao_com_nome("Gabriel")

# Função com Parâmetros com Valores Default

def saudacao_com_nome_default(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao_com_nome_default()

#Argumentos e Parâmetros Variáveis (*args e **kwargs)

def soma(*numeros):
    return sum(numeros)
print (soma(1,2,3,4))

def exibir_informacoes(**info):
    print(info)
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
exibir_informacoes(nome="Gabriel", idade=27)

# Retorno de Valores

def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)

#Escopo de Variáveis
def numero():
    x=10
    print("Variável local: ",x)
numero()

x=5
print("Variável Global: ",x)

#Funções Lambda

dobro = lambda x: x * 2
print(dobro(5))