import psycopg2

# DADOS DE CONEXÃO
host = "localhost"
dbname = "postgres"
user = "postgres"
password = "postgres"
sslmode = "require"

# CRIANDO CONEXÃO COM O BANCO

db_connection = "host={0} dbname={1} user={2} password={3} sslmode={4}".format(host,dbname,user,password,sslmode)
connecting = psycopg2.connect(db_connection)

cursor = connecting.cursor()
# print('Conexão bem sucedida!')
print('Seja bem vindo à nossa base de dados ! Vamos começar ?')

# FIND ALL

gerando_busca = True
listar_todos = input("Deseja listar todos os usuários ? Y/N: ")

#-----------------------------------------------------------------------------------------------------------------------
def find_all():
    cursor.execute("SELECT * FROM usuarios")
    if listar_todos == 'Y':
        return cursor.fetchall()
        print("Esses são todos os usuários da sua base!")

    if listar_todos == 'N':
        print("Você escolheu não listar os usuários!")
    else :
        print("Erro ao buscar usuários! Verifique se a resposta corresponde com as opções sugeridas!")

mostar_todos = find_all()
print(mostar_todos)
#-----------------------------------------------------------------------------------------------------------------------

connecting.commit()
cursor.close()
connecting.close()
