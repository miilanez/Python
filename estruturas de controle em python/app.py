#Estruturas de Decisão ( if, Else If, Else )

nota = 85 

if nota >= 90:
    print("Aprovado com Distinção")
elif nota >= 60:
    print("Aprovado")
elif nota <= 59:
    print("Recuperação")
elif nota <= 30:
    print("Reprovado")
else:
    print("Reprovado com Distinção")

#Estruturas de Repetição (For)

letras = ['a', 'b', 'c',]

for letra in letras:
    print(letra)


#Estruturas de Repetição (While)

contador = 1

while contador <= 10:
    print("Convidados: ", contador)
    contador += 1

#Comandos de Controle de Fluxo

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

#break
for numero in numeros:
    if numero == 7:
        print("numero encontrados: ", numero)
        break
    
#continue
for numero in range(1, 10):
    if numero % 2 == 0:
        continue
    print("numero impar: ", numero)

#pass
for numero in range(1,5):
    if numero == 3:
        pass
        print("numero encontrado: ", numero)
    else:
        print("numero: ", numero)

