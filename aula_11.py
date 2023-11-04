import psycopg2

# Estabeleça uma conexão com o banco de dados
conn = psycopg2.connect(database="postgres", user="postgres", password="12345", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")

# Crie um objeto de cursor para executar consultas SQL
cur = conn.cursor()

# Execute uma consulta SQL para criar uma tabela
cur.execute('''CREATE TABLE Agenda (ID INT PRIMARY KEY NOT NULL, Nome TEXT NOT NULL, Telefone CHAR(12));''')
print("Tabela criada com sucesso!")

# Faça um commit para salvar as alterações no banco de dados
conn.commit()

# Feche a conexão
conn.close()
