import mysql.connector
class Conexao:
    def conectar():
        mydb = mysql.connector.connect(
        host ="127.0.0.1",
        user ="local",
        password ="root",
        database ="raybellecharm")

        return mydb