###
# autores:
# michel silva

# data: 07/12/2022
#

# continuando com o bando de exemplo da aula,
# vamos fazer um select.

# importar o Sqlite3
import sqlite3 as db

# criar o banco ou conecta o banco
db1 = db.connect("agenda.db")


# antes devemos criar o primeiro o objeto cursor.
# que vai receber o banco e assim podemos executar os comando SQL (criar tabela, inserir, excluir, etc)
cursor = db1.cursor()
