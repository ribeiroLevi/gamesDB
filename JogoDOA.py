import traceback
import psycopg2
from Usuario import Usuario
from Connection import Connection


class JogoDAO:

    def listarJogos(self):
        resultado = []
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome FROM jogo")
            registros = cursor.fetchall()
            for linha in registros:
                u = Usuario()
                u.id = linha[0]
                u.nome = linha[1]
                resultado.append(u)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    def inserirJogo(
        self, nome, descricao, idioma, duracao, tipo, min_jogadores, max_jogadores
    ):
        sucess = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO jogo (nome, descricao, idioma, duracao, tipo, min_jogadores, max_jogadores) VALUES ('{}', '{}', '{}')".format(
                    nome, descricao, idioma, duracao, tipo, min_jogadores, max_jogadores
                )
            )
            connection.commit()
            if cursor.rowcount == 1:
                sucess = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucess

    def atualizarJogo(self, nome, descricao, idioma, duracao, tipo, min_jogadores, max_jogadores):
        sucess = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE jogo SET nome = '{}', descricao = '{}', idioma = '{}', duracao = '{}', tipo = '{}', min_jogadores = '{}', max_jogadores = '{}')".format(
                    nome, descricao, idioma, duracao, tipo, min_jogadores, max_jogadores
                )
            )
            connection.commit()
            if cursor.rowcount == 1:
                sucess = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucess

    def deletarJogo(self, id):
        sucess = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("DELETE jogo WHERE id = '{}')".format(id))
            connection.commit()
            if cursor.rowcount == 1:
                sucess = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucess
