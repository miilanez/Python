Repositório de Estudos da Linguagem Python.

Apresentando os conteúdos do mais básico ao mais completo


Código-fonte das aulas sobre [Python](https://www.youtube.com/watch?v=OsH8sZb8x1k&list=PLmY5AEiqDWwAKFymn4450k9XGLt8v3Xgd&index=1).<br>

## Requesitos

* Python 3 ou superior - Conferir a versão: python --version
* MySQL 8 ou superio - Conferir a versão: mysql --version

## Como rodar o projeto baixado

Conferir se o Python está instalado corretamente no PC.
```
python --version
```

Acessar o diretório da aula.
```
cd "pasta"
```

Executar o programa Python no terminal.
```
python app.py
```

## Sequencia para criar o projeto

Instalar a biblioteca para conectar o Python com MySQL.
```
pip install mysql-connector-python
```

## Acessar o MySQL.

Acessar o MySQL.
```
mysql -h localhost -u root -p
```

Listar as base de dados.
```
SHOW DATABASES;
```

Sair do MySQL.
```
exit
```

Criar a base de dados.
```
CREATE DATABASE pythonmysql CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Criar a tabela "users".
```
CREATE TABLE pythonmysql.users(
    id int NOT NULL AUTO_INCREMENT, 
    name varchar(220) COLLATE utf8mb4_unicode_ci DEFAULT NULL, 
    email varchar(220) COLLATE utf8mb4_unicode_ci DEFAULT NULL, 
    PRIMARY key (id)
) ENGINE=InnoDB DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
