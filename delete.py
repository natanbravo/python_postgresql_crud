import psycopg2

# DADOS DE CONEXÃO
host = "localhost"
dbname = "postgres"
user = "postgres"
password = "postgres"
sslmode = "require"

# CRIANDO CONEXÃO COM O BANCO

db_connection = "host={0} dbname={1} user={2} password={3} sslmode={4}".format( host,dbname,user,password,
                                                                                sslmode )
connecting = psycopg2.connect( db_connection )

cursor = connecting.cursor( )
print( 'Conexão bem sucedida!' )
print( 'Seja bem vindo à nossa base de dados ! Vamos começar ?' )

# ----------------------------------------------------------------------------------------------------------------------
# DELETE
deletando_usuario = True
deletar_usuario = int( input( "Insira o id do usuário que deseja deletar: " ) )

while deletando_usuario:
    usuario_deletado = False
    if deletar_usuario:
        deletar_usuario
        deletando_usuario = False
    usuario_deletado = True
    print( "Usuário deletado com sucesso!" )


def delete_user(id):
    cursor.execute( "DELETE FROM usuarios WHERE id=%s ;",(id,) )


deletado = delete_user(deletar_usuario)
print( deletado )

# ----------------------------------------------------------------------------------------------------------------------

connecting.commit ( )
cursor.close ( )
connecting.close ( )
