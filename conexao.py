import mysql.connector
class Conexao:
    def conectar():
        mydb = mysql.connector.connect(
        host ="127.0.0.1",
        user ="usuario_raybelle",
        password ="raybelle",
        database ="raybellecharm")

        return mydb