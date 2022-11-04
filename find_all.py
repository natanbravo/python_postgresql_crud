import psycopg2
import modulo

# FIND ALL
gerando_busca = True
listar_todos = input("Deseja listar todos os usuários ? Y/N: ")

def find_all():
    modulo.cursor.execute("SELECT * FROM usuarios")
    if listar_todos == 'Y':
        return modulo.cursor.fetchall()
        print("Esses são todos os usuários da sua base!")

    if listar_todos == 'N':
        print("Você escolheu não listar os usuários!")
    else:
        print("Erro ao buscar usuários! Verifique se a resposta corresponde com as opções sugeridas!")


mostar_todos = find_all()
print(mostar_todos)

modulo.connecting.commit()
modulo.cursor.close()
modulo.connecting.close()
