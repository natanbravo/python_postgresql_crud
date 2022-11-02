import psycopg2

# DADOS DE CONEXÃO
host = "localhost"
dbname = "postgres"
user = "postgres"
password = "postgres"
sslmode = "require"

# CRIANDO CONEXÃO COM O BANCO

db_connection = "host={0} dbname={1} user={2} password={3} sslmode={4}".format(host,dbname,user,password,
                                                                               sslmode)
connecting = psycopg2.connect(db_connection)

cursor = connecting.cursor()
# print('Conexão bem sucedida!')
print('Seja bem vindo à nossa base de dados ! Vamos começar ?')

# ----------------------------------------------------------------------------------------------------------------------

# FIND ONE
busca_em_andamento = True
id_usuario = int(input("Qual pin do usuário que deseja encontrar? "))

while busca_em_andamento:
    busca_completa = False
    if id_usuario:
        id_usuario
        busca_em_andamento = False
    busca_completa = True
    print("Usuário encontrado com sucesso!")


def find_one(id):
    cursor.execute("SELECT * FROM usuarios WHERE id=%s ;",(id,))
    return cursor.fetchall()


buscar_um = find_one(id_usuario)
print(buscar_um)
# ----------------------------------------------------------------------------------------------------------------------


connecting.commit()
cursor.close()
connecting.close()
