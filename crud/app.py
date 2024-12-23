import mysql.connector 
from mysql.connector import Error

#pip install mysql-connector-python

#Função para Conectar ao Banco de Dados
def conectar():
    """Conexão estabelecida com Banco de Dados"""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="pythonmysql"
        )
        
        if conexao.is_connected():
            print("Conexão bem-sucedida!")
            return conexao
        
    except Error as e:
        print(f"Ocorreu um erro na conexão: {e}")
        return None
    

#Função para Cadastrar no Banco de Dados

def cadastrar(conexao, name, email):
    """Cadastrar um novo cliente no Banco de Dados"""
    try:
        cursor = conexao.cursor()
        query = "INSERT INTO users (name, email) VALUE (%s, %s)"
        valores = (name, email)
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Cliente '{name}' cadastrado com sucesso!")
        return None
    except Exception as e:
        print(f"Ocorreu um erro na operação: {e}")
        
#Conexão com o Banco de Dados
conexao = conectar()

#Verificar se possui a conexão com o banco de dados
if conexao:
    #Cadastra novo registro
    print("Cadastrar o Registro")
    # cadastrar(conexao, "Rafael", "rafael@blueumbrella.com.br")
    
    
#Função para listar os Registros do Banco de Dados
def listar(conexao):
    """Listar todos os clientes do Banco de Dados"""
    try:
        cursor = conexao.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        dados = cursor.fetchall()
        for (id, name, email) in dados:
            print(f"ID: {id}, Nome: {name}, Email: {email}")
            
    except Exception as e:
        print(f"Ocorreu um erro na operação: {e}")
        
def visualizar(conexao, id):
    """Visualizar um único cliente do Banco de Dados"""
    try:
        cursor = conexao.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        valores = (int(id),)
        cursor.execute(query, valores)
        dados = cursor.fetchone()
        if dados:
            print(f"ID: {dados[0]}, Nome: {dados[1]}, Email: {dados[2]}")
        else:
            print("Cliente não encontrado!")
            
    except Exception as e:
        print(f"Ocorreu um erro na operação: {e}")
        
#Atualizar um registro no Banco de Dados

def atualizar(conexao, id, name, email):
    """Atualizar um cliente no Banco de Dados"""
    try:
        cursor = conexao.cursor()
        query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        valores = (name, email, id)
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Usuário '{id}' atualizado com sucesso!")
    except Error as e:
        print(f"Ocorreu um erro na operação: {e}")
        return None
    
#Apagar um registro no banco de Dados

def deletar(conexao, id):
    """Deletar um cliente no Banco de Dados"""
    try:
        cursor = conexao.cursor()
        query = "DELETE FROM users WHERE id = %s"
        valores = (int(id),)
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Usuário {id} deletado com sucesso!")
    except Error as e:
        print(f"Ocorreu um erro na operação: {e}")
        return None
        
#Ler os registros
print("Listar os registros:")
listar(conexao)

#Visualizar um único registro
print("Visualizar um registro")
visualizar(conexao, 1)

#Atualizar/Editar um registro
print("Atualizar um registro")
atualizar(conexao, 1, "Gabriel Milanez", "gabriel@blueumbrellatech.com.br")
listar(conexao)

#Apagar/Deletar um registro
print("Excluir um registro")
deletar(conexao, 3)
listar(conexao)