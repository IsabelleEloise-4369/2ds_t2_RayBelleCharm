import mysql.connector
class Conexao:
    def conectar():
        mydb = mysql.connector.connect(
        host ="127.0.0.1",
        # não esquecer de modificar isso conforme a porta do banco de dados
        user ="usuario_raybelle",
        password ="raybelle",
        database ="raybellecharm")

        return mydb