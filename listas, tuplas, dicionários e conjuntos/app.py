#Manipulação de Listas

#Criar uma Lista
frutas = ["maçã", "banana", "laranja"]
print(frutas)

#Adicionar um item ao final da lista
frutas.append("uva")
print(frutas)

#Remover um item da lista
frutas.remove("banana")
print(frutas)

#Acessar um item específico
print(frutas[1])

#Alterar um item específico
frutas[0] = "limão"
print(frutas)

#Contar quantas vezes um item aparece na lista
print(frutas.count("limão"))

#Ordenar a lista em ordem alfabética
frutas.sort()

#Iterar sobre a lista
for fruta in frutas:
    print(fruta)

#Remover todos os itens da lista
frutas.clear()


#Manipulação de Tuplas

#Criar uma tupla
usuario = ("Gabriel", "gabriel.milanez@gmail.com")

#Acessar item pelo índice
print(usuario[0])

#Descompactar tuplas
nome, email = usuario
print(f"Nome: {nome}, Email: {email}")

#Manipulação de Dicionários

#Criar um dicionário
aluno = {
    "nome":"Gabriel", "nota": 9.5,
}
print(aluno)

#Alterar um dicionário
aluno["nome"] = "Rafael"
print(aluno)

#Iterar sobre chaves e valores
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
    
#Remover uma chave/valor
del aluno["nota"]
print(aluno)


#Manipulação de Conjuntos

#Criar um conjunto
numeros = {1,2,3,4,5,6}
print(numeros)

#Adicionar um elemento
numeros.add(7)
print(numeros)

#Remover um elemento
numeros.remove(4)
print(numeros)

#Operação de união de interseção de conjuntos
pares = {2,4,6,8}
impares = {1,3,5,7,9}
uniao = numeros.union(pares, impares)
print(uniao)

intersecao = numeros.intersection(pares)
print(intersecao)

#Verificar se elemento está no conjunto
print(3 in numeros)