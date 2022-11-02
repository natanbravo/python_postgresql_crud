import psycopg2

# DADOS DE CONEXÃO
host = "localhost"
dbname = "postgres"
user = "postgres"
password = "postgres"
sslmode = "require"

# CRIANDO CONEXÃO COM O BANCO

db_connection = "host={0} dbname={1} user={2} password={3} sslmode={4}".format ( host,dbname,user,password,
                                                                                 sslmode )
connecting = psycopg2.connect ( db_connection )

cursor = connecting.cursor ( )
# print('Conexão bem sucedida!')
print ( 'Seja bem vindo à nossa base de dados ! Vamos começar ?' )

# ----------------------------------------------------------------------------------------------------------------------
# UPDATE
atualizacao_andamento = True
id_usuario = int ( input ( "Informe o pin que deseja alterar os dados: " ) )
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
    print ( "Cadastro atualizado com sucesso!" )
    print ( "Você pode verificar essa atualização no seu banco de dados!" )
    break


def update_user(id,nome,idade,altura,genero,profissao):
    cursor.execute ( "UPDATE usuarios SET nome=%s, idade=%s, altura=%s, genero=%s, profissao=%s WHERE id=%s;",
                     (nome,idade,altura,genero,profissao,id) )


update_user ( f'{id_usuario}',f'{nome}',f'{idade}',f'{altura}',f'{genero}',f'{profissao}' )

connecting.commit ( )
cursor.close ( )
connecting.close ( )
