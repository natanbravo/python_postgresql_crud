import psycopg2

# DADOS DE CONEXÃO
host = "localhost"
dbname = "postgres"
user = "postgres"
password = "postgres"
sslmode = "require"

# CRIANDO CONEXÃO COM O BANCO

db_connection = "host={0} dbname={1} user={2} password={3} sslmode={4}".format ( host , dbname , user , password ,
                                                                                 sslmode )
connecting = psycopg2.connect ( db_connection )

cursor = connecting.cursor ( )
# print('Conexão bem sucedida!')
print ( 'Seja bem vindo à nossa base de dados ! Vamos começar ?' )

# CREATE
cadastro_em_andamento = True
nome = input ( 'Informe seu nome: ' )
idade = input ( 'Informe sua idade: ' )
altura = input ( 'Informe sua altura: ' )
genero = input ( 'Qual gênero você se identifica: ' )
profissao = input ( 'Para finalizar, conte-nos qual a sua profissão: ' )

while cadastro_em_andamento:
    cadastro_completo = False
    if nome :
        nome ;
    elif idade :
        idade ;
    elif altura :
        altura ;
    elif genero :
        genero ;
    elif profissao :
        profissao ;
        cadastro_em_andamento = False

    cadastro_completo = True
    print ( 'Seu cadastro foi efetuado com sucesso!' )
    print('Verifique seus dados em nossa base PostgreSQL')
    break;
else :
    print ( 'Não foi possível completar o seu cadastro! Por favor entre em contato com Nick Fury! ' )

def create_user ( nome , idade , altura , genero , profissao ) :
    cursor.execute ( "INSERT INTO usuarios (nome,idade,altura,genero,profissao) VALUES (%s, %s,%s,%s,%s);" ,
                     (nome , idade , altura , genero , profissao) )


create_user ( f'{nome}' , f'{idade}' , f'{altura}' , f'{genero}' , f'{profissao}' )

#-------------------------------------------------------------------------------------------------------------------#

# READ
def find_all():
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

buscar_todos = find_all()
print(buscar_todos)


#-------------------------------------------------------------------------------------------------------------------#
#READ
def find_one(id):
    cursor.execute("SELECT * FROM usuarios WHERE id=%s ;", (id, ))
    return cursor.fetchall()

buscar_um = find_one(5)
print(buscar_um)



# -------------------------------------------------------------------------------------------------------------------#
# UPDATE

atualizacao_andamento = True
id_usuario = int(input("Informe o pin que deseja alterar os dados: "))
nome = input ( 'Informe seu nome: ' )
idade = input ( 'Informe sua idade: ' )
altura = input ( 'Informe sua altura: ' )
genero = input ( 'Qual gênero você se identifica: ' )
profissao = input ( 'Para finalizar, conte-nos qual a sua profissão: ' )

while atualizacao_andamento:
    atualizacao_completa = False
    if id_usuario:
        id_usuario
    elif nome:
        nome
    elif idade:
        idade
    elif altura:
        altura
    elif genero:
        genero
    elif profissao:
        profissao
        atualizacao_andamento = False

    atualizacao_completa = True
    print("Cadastro atualizado com sucesso!")
    print("Você pode verificar essa atualização no seu banco de dados!")
    break


def update_user ( id , nome , idade , altura , genero , profissao ) :
    cursor.execute ( "UPDATE usuarios SET nome=%s, idade=%s, altura=%s, genero=%s, profissao=%s WHERE id=%s;" ,
                     (nome , idade , altura , genero , profissao , id) )


update_user ( f'{id_usuario}' , f'{nome}' , f'{idade}' , f'{altura}' , f'{genero}' , f'{profissao}' )


# -------------------------------------------------------------------------------------------------------------------#

connecting.commit ( )
cursor.close ( )
connecting.close ( )
