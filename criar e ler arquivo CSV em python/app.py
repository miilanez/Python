#Importar a biblioteca CSV
import csv

#Modo w abre o arquivo para escrita. Se o arquivo não existe, será criado. Se existir, será sobrescrito
with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
    escrever = csv.writer(arquivo)
    escrever.writerow(["Nome", "Idade", "Cidade"])
    escrever.writerow(["Gabriel", 28, "Recife"])
    
#Modo a abre o arquivo para acrescentar conteúdo. Se o arquivo não existir, será criado, mas não sobrescreve

with open("dados.csv", "a", newline="", encoding="utf-8") as arquivo:
    escrever = csv.writer(arquivo)
    escrever.writerow(["Rafael", 25, "Salvador"])
    escrever.writerows([["Pedro", 32, "Fortaleza"], ["Jessica", 29, "Maceió"]]) #writerows para mais de uma linha
    
#Modo r abre o arquivo para leitura. Se o arquivo não existir, será lançado um FileNotFoundError

try:
    with open("dados.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    
    
# Outros modos:
# 'r' leitura
# 'w' escrita
# 'a' adição de conteúdo
# 'x' criação exclusiva - falha se o arquivo existir
# 'b' binário
# 't' texto - padrão para csv
# 'r+' leitura e escrita - não apaga o conteúdo
# 'w+' leitura e escrita - sobrescreve o conteúdo
# 'a+' leitura e adição - acrescenta no final
# 'x+' criação exclusiva e leitura