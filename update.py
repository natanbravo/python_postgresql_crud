import psycopg2
import modulo
# UPDATE
atualizacao_andamento = True
id_usuario = int(input("Informe o pin que deseja alterar os dados: "))
nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
altura = input('Informe sua altura: ')
genero = input('Qual gênero você se identifica: ')
profissao = input('Para finalizar, conte-nos qual a sua profissão: ')

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


def update_user(id, nome, idade, altura, genero, profissao):
    modulo.cursor.execute("UPDATE usuarios SET nome=%s, idade=%s, altura=%s, genero=%s, profissao=%s WHERE id=%s;",
                          (nome, idade, altura, genero, profissao, id))


update_user(f'{id_usuario}', f'{nome}', f'{idade}',
            f'{altura}', f'{genero}', f'{profissao}')


modulo.connecting.commit()
modulo.cursor.close()
modulo.connecting.close()
