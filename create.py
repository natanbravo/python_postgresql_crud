import psycopg2
import modulo

# CREATE
cadastro_em_andamento = True
nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
altura = input('Informe sua altura: ')
genero = input('Qual gênero você se identifica: ')
profissao = input('Para finalizar, conte-nos qual a sua profissão: ')

while cadastro_em_andamento:
    cadastro_completo = False
    if nome:
        nome
    elif idade:
        idade
    elif altura:
        altura
    elif genero:
        genero
    elif profissao:
        profissao
        cadastro_em_andamento = False

    cadastro_completo = True
    print('Seu cadastro foi efetuado com sucesso!')
    print('Verifique seus dados em nossa base PostgreSQL')
    break
else:
    print('Não foi possível completar o seu cadastro! Por favor entre em contato com Nick Fury! ')


def create_user(nome, idade, altura, genero, profissao):
    modulo.cursor.execute("INSERT INTO usuarios (nome,idade,altura,genero,profissao) VALUES (%s, %s,%s,%s,%s);",
                          (nome, idade, altura, genero, profissao))


create_user(f'{nome}', f'{idade}', f'{altura}', f'{genero}', f'{profissao}')

modulo.connecting.commit()
modulo.cursor.close()
modulo.connecting.close()
