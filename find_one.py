import psycopg2
import modulo

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
    modulo.cursor.execute("SELECT * FROM usuarios WHERE id=%s ;", (id,))
    return modulo.cursor.fetchall()


buscar_um = find_one(id_usuario)
print(buscar_um)

modulo.connecting.commit()
modulo.cursor.close()
modulo.connecting.close()
