###
# autores:
# michel silva

# data: 07/12/2022
#

# continuando com o bando de exemplo da aula,
# vamos fazer um select.

# 1. importar o Sqlite3
import sqlite3 as db

# 2. criar o banco ou conecta o banco
db1 = db.connect("agenda.db")

# 3. antes devemos criar o primeiro o objeto cursor.
# que vai receber o banco e assim podemos executar os comando SQL (criar tabela, inserir, excluir, etc)
cursor = db1.cursor()

# deletar um registro
try: # tenta executar o código abaixo 
  # correto 
  cursor.execute("DELETE from pessoas WHERE idade = 9") 
  db1.commit()
  
  # errado
  cursor.execute("DELETE from pessoas WHERE idade2 = 9") 
  db1.commit()
  #  gerar o erro 'no such column: idade2' 
  
  
  cursor.execute("SELECT * FROM pessoas") # * -> todos os campos
  print(cursor.fetchall()) 
  db1.close() # fecha o banco
  print("dados removidos!")
except Exception as e: # caso ocorra um erro imprima o erro
  print(str(e))  # imprime o erro gerado