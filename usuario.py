from conexao import Conexao
from hashlib import sha256

class Usuario:
    def __init__ (self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.telefone = None
        self.senha = None
        self.enderecoRua = None
        self.enderecoNumero = None
        self.estado = None
        self.cidade = None

# criando a função para cadastrar um usuário
    def cadastrar (self, nome, cpf, email, telefone, senha, enderecoRua, enderecoNumero, estado, cidade):
        #criptografar a senha
        senha = sha256(senha.encode()).hexdigest()

        # try:
        # conectando o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()
    
        #inserir os dados na tabela 
        dados = f"INSERT INTO tb_cliente (nome, cpf, email, telefone, senha, endereco_rua, endereco_numero, estado, cidade) VALUES ('{nome}', '{cpf}', '{email}', '{telefone}', '{senha}', '{enderecoRua}', '{enderecoNumero}', '{estado}', '{cidade}')"

        #executar
        mycursor.execute(dados)

        mydb.commit()

        mydb.close()

        return True

        # except:
            # return False