import psycopg2
import modulo

# DELETE
deletando_usuario = True
deletar_usuario = int(input("Insira o id do usuário que deseja deletar: "))

while deletando_usuario:
    usuario_deletado = False
    if deletar_usuario:
        deletar_usuario
        print(' ')
        deletando_usuario = False
    usuario_deletado = True
    print("Usuário deletado com sucesso!")


def delete_user(id):
    modulo.cursor.execute("DELETE FROM usuarios WHERE id=%s ;", (id,))


deletado = delete_user(deletar_usuario)
print(deletado)


modulo.connecting.commit()
modulo.cursor.close()
modulo.connecting.close()

