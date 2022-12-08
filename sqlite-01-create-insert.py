###
# autores:
# michel silva

# data: 07/12/2022
#
# Composição 
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

# se aparecer o erro 'sqlite3.DatabaseError: database disk image is malformed'
# pode apagar o bando e recomeçar 
# isso aconteceu muito comigo pq o replit caiu muito a conexão enquanto eu estava trabalhando nele

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
