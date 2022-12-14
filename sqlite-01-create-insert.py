###
# autores:
# michel silva

# data: 07/12/2022
#

#
# DQL - Linguagem de Consulta de Dados
# DQL - (select)

# DML - Linguagem de Manipulação de Dados (dados)
# DML (insert, update e delete) (insere, atualiza e deleta registros)

# DDL - linguagem de definição e dados (Metadados)
# DDL (create, alter, drop) (cria, altera e deleta as tabelas)

# DCL - Linguagem de Controle de Dados (controle de acesso ao banco)
# DCL (grant e revoke) (adiciona e remove, permissões de acesso)

# DTL - Linguagem de Transação de Dados (gerenciar transações de dados)
# DTL - (begin, commit e rollback) (inicia, confirma e desfaz uma transação)

# vamos usar apenas os seguintes instruções (DQL, DML, DDL e DTL):
# create
# insert
# select
# delete
# update
# commit

# se aparecer o erro 'sqlite3.DatabaseError: database disk 
# image is malformed'
# pode apagar o bando e recomeçar 
# isso aconteceu muito comigo pq o repl.it caiu muito a conexão enquanto eu estava trabalhando nele

# C -> CREATE
# R -> READ
# U -> UPDATE
# D -> DELETE

'''
1 - importar o SQLite3
2 - criar o banco ou conecta o banco
3 - criar o cursor
4 - SQL (criar tabela, executar instruções SQL)
4.1 - execute
4.2 - para garantir a transação no banco (commit)
4.3 - fechar o banco

'''

# criando o bande de exemplo d aula

# 1. importar o Sqlite3
import sqlite3 as db

# 2. criar o banco ou conecta o banco
db1 = db.connect("agenda.db")

# criando as entidades (tabelas)
#3.  antes devemos criar o primeiro o objeto cursor
# que vai receber o banco e assim podemos executar os comando SQL (criar tabela, inserir, excluir, etc)
cursor = db1.cursor()

# criando tabelas (se a tabela existir vai dar error)
# a linha #1 abaixo, se rodar o pela segunda vez da erro.
# 1
cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

# pelo SQL podemos evitar o erro acima (rodando pela segunda vez), usando a linha #2
# se a tabela já existir no banco usar o IF NOT EXISTS
# 2
cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text, idade integer, email text)")

# inserindo elementos na tabela pessoas, use aspa simples para não criar erro com a as dupla do parâmetro.
cursor.execute("INSERT INTO pessoas VALUES('Davi', 9, 'davi@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES('Dani', 15, 'dani@gmail.com')")

# realizando um commit para conformar a inserção do banco
# Lembre-se de sempre salvar as alterações no banco de dados
# usando o método db1.commit(). Caso contrário, as alterações
# não serão salvas permanentemente.
db1.commit()

# fechar a conexão
# Isso irá fechar a conexão com o banco de dados e 
# liberar os recursos usados pela conexão. 
# É importante fechar a conexão quando você não 
# precisar mais dela, para evitar consumir 
# recursos desnecessariamente.
db1.close()