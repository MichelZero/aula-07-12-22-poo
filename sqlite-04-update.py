###
# autores:
# Michel silva

# data: 07/12/2022
#

# continuando com o bando de exemplo da aula,
# vamos fazer um select.

# 1. importar o Sqlite3
import sqlite3 as db

# criar o banco ou conecta o banco
db1 = db.connect("agenda.db")


# antes devemos criar o primeiro o objeto cursor.
# que vai receber o banco e assim podemos executar os comando SQL (criar tabela, inserir, excluir, etc)
cursor = db1.cursor()

# update em um registro
try: # tenta executar o código abaixo 
  cursor.execute("UPDATE pessoas SET idade = 20 WHERE nome = 'Dani'")
  db1.commit()
  
  cursor.execute("SELECT * FROM pessoas")
  print(cursor.fetchall()) 
  db1.close()
  
except Exception as e: # caso ocorra um erro imprima o erro 
  print(str(e))  # imprime o erro gerado