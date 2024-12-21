#Importando o pacote datetime
from datetime import datetime

#Função para adicionar um cliente ao Sistema
def adicionar_cliente(nome, ano_nascimento):
    """Adicionar um cliente ao Sistema"""

    #Captando o ano atual utilizando o pacote datetime
    ano_atual = datetime.now().year

    #Calculando a idade do cliente baseado no ano de nascimento e no ano atual
    idade = ano_atual - ano_nascimento

    #Exibindo os dados do cliente
    print(f"Nome:  {nome} \nIdade: {idade}")