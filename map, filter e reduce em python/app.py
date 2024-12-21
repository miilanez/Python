#Função Map

#map(função, iterável)
valores = [1000, 1500, 2000, 2500, 3000]
print("Valores Iniciais: ", valores)

#Função para calcular juros de 2%
calcular_juros = lambda valor: valor * 1.02

#Utilizando o Map
valores_com_juros = list(map(calcular_juros, valores))

#Exibir os valores com juros
print("Valores com juros aplicados: ",valores_com_juros)


#Função Filter

#filter(função, iterável)
numeros = [1,2,3,4,5,6,7,8,9]

#Função para verificar se um número é par
def verificar_numeros_pares(x):
    return x % 2 == 0

#Função para filtrar valores pares
numeros_pares = filter(verificar_numeros_pares, numeros)
print(list(numeros_pares))


#Função Reduce

#reduce(função, iterável, inicial)

from functools import reduce

numeros=[1,2,3,4,5,6,7,8,9]

#Criando a função de soma
def soma (a, b):
    return a + b

#Função para calcular a soma
total = reduce(soma, numeros, 0)
print(total)