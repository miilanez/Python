import mysql.connector 
from mysql.connector import Error

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
    
conexao = conectar()