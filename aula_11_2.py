from tkinter import messagebox
import psycopg2

# Estabeleça uma conexão com o banco de dados
conn = psycopg2.connect(database="postgres", user="postgres", password="12345", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")

# Crie um objeto de cursor para executar consultas SQL
cur = conn.cursor()

sql="INSERT INTO public.AGENDA (id, nome , telefone) VALUES (1, 'Pessoa 1' , '02199999999' )" 
cur.execute(sql)
sql2="select * from public.AGENDA where id=1"
cur.execute(sql2)
registro=cur.fetchone()

messagebox.showinfo("Tabela", registro)

# Faça um commit para salvar as alterações no banco de dados
conn.commit()

# Feche a conexão
conn.close()
