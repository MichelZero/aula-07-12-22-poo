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


# antes devemos criar o primeiro o objeto cursor
# que vai receber o banco e assim podemos executar os comando SQL (criar tabela, inserir, excluir, etc)
cursor = db1.cursor()


# para visualizar os dados da tabela
# execute um SELECT para o cursor
# print o método fetchall() (fetch -> buscar)
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) 
print(type(cursor.fetchall())) # retorna uma lista 


# imprimir em linha
cursor.execute("SELECT * FROM pessoas")
tabela = cursor.fetchall()
for i in tabela:
  print(i)

db1.close()
# shift + alt + a cria comentários em múltiplas linhas no repl.it