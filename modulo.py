import psycopg2

# DADOS DE CONEXÃO

host = "localhost"
dbname = "postgres"
user = "postgres"
password = "postgres"
sslmode = "require"

# CRIANDO CONEXÃO COM O BANCO

db_connection = "host={0} dbname={1} user={2} password={3} sslmode={4}".format(
    host, dbname, user, password, sslmode)
connecting = psycopg2.connect(db_connection)

cursor = connecting.cursor()
print('')
print('Conexão bem sucedida!')
print('')
print('Seja bem vindo à nossa base de dados ! Vamos começar ?')
print('')



