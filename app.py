from flask import Flask, render_template, request, redirect, session, jsonify
from usuario import Usuario
from conexao import Conexao

#app é o servidor
#criei o objeto app usando a classe Flask
app = Flask(__name__)
app.secret_key = 'raybelle'

#roteamento da página
@app.route("/")
#função da página inicial
def pagina_inicial():
    return render_template("raybelle.html")

#roteamento da página cadastro
@app.route("/cadastro", methods=["GET", "POST"])
#função da página de caadastro
def pagina_cadastro():
    if request.method == "GET":
        return render_template("cadastro-raybelle.html")
    if request.method == "POST":
        # Extrair os dados do formulário
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        senha = request.form.get("senha")
        enderecoRua = request.form.get("enderecoRua")
        enderecoNumero = request.form.get("enderecoNumero")
        estado = request.form.get("estado")
        cidade = request.form.get("cidade")
        
        # Criar uma instância da classe Usuario
        usuario = Usuario()

        # Chamar o método cadastrar
        if usuario.cadastrar(nome, cpf, email, telefone, senha, enderecoRua, enderecoNumero, estado, cidade):
            return redirect("/")  # Redirecionar para a página inicial após o cadastro
        else:
            return "Erro ao cadastrar o usuário."

#roteamento da página login
@app.route("/login", methods=["GET", "POST"])
#função da página de login
def pagina_login():
    if request.method == "GET":
        return render_template("login-raybelle.html")
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario()
        usuario.logar(email, senha)
        if usuario.logado:
            session['usuario_logado'] = {'email':usuario.email,
                                         'senha':usuario.senha,
                                         'cpf':usuario.cpf}
            return redirect('/comentario')
        else:
            session.clear()
            return 'Email ou senha incorretos.'

#roteamento da página comentário
@app.route("/comentario", methods=["GET", "POST"])
#função da página de comentário
def pagina_comentario():

    if "usuario_logado" in session:
        if request.method == 'GET':
            return render_template("comentario-raybelle.html")
        if request.method == 'POST':
            avaliacao = request.form['comentario']
            idProd = request.form['cod_prod']
            nomeProd = request.form['nome_prod']

            mydb = Conexao.conectar()
            
            mycursor = mydb.cursor()

            comentario = (f"INSERT INTO tb_comentario (cpf_cliente, avaliacao, cod_prod) VALUES ('{session['usuario_logado']['cpf']}', '{avaliacao}', {idProd})")

            mycursor.execute(comentario)

            mydb.commit()

            mydb.close()

            nomeProd = nomeProd.replace(' ', '+')
            return redirect(f"/sobreProduto?saibaMais={nomeProd}")

    else:
        return redirect("/cadastro")

#roteamento da página de produtos ouro
@app.route("/ouro")
#função da página de produtos apenas de ouro
def pagina_ouro():
    # conectando o banco de dados
    mydb = Conexao.conectar()

    mycursor = mydb.cursor()
    # Consulta ao banco de dados para obter os produtos da categoria "ouro"
    produtos_ouro = ("SELECT preco, foto, descricao, categoria FROM tb_produto WHERE categoria = 'ouro'")

    #executar
    mycursor.execute(produtos_ouro)
    resultado = mycursor.fetchall()

    mydb.close()

    lista_produtos = []
    
    for produto in resultado:
        lista_produtos.append({
            "preco":produto[0],
            "foto":produto[1],
            "descricao":produto[2],
            "categoria":produto[3],
        })

    return render_template("ouro-raybelle.html", lista_produtos = lista_produtos)
    
    # return render_template("ouro-raybelle.html", produtos=produtos_ouro)
    
#roteamento da página de produtos prata
@app.route("/prata")
#função da página de produtos apenas de prata
def pagina_prata():
    # conectando o banco de dados
    mydb = Conexao.conectar()

    mycursor = mydb.cursor()
    # Consulta ao banco de dados para obter os produtos da categoria "ouro"
    produtos_prata = ("SELECT preco, foto, descricao, categoria FROM tb_produto WHERE categoria = 'prata'")

    comentario = ("SELECT cpf_cliente, avaliacao FROM tb_comentario")

    #executar
    mycursor.execute(produtos_prata)
    resultado = mycursor.fetchall()

    mycursor.execute(comentario)
    comentarios = mycursor.fetchall()

    mydb.close()

    lista_produtos = []
    
    for produto in resultado:
        lista_produtos.append({
            "preco":produto[0],
            "foto":produto[1],
            "descricao":produto[2],
            "categoria":produto[3],
        })

    lista_comentario = []

    for coment in comentarios:
        lista_comentario.append({
            "cpf_cliente":coment[0],
            "avaliacao":coment[1]
        })

    return render_template("prata-raybelle.html", lista_produtos = lista_produtos, lista_comentario = lista_comentario)

# roteamento para aparecer apenas o produto escolhido
@app.route("/sobreProduto")
def pagina_produtos():

    nome = request.args.get('saibaMais')

    # conectando o banco de dados
    mydb = Conexao.conectar()

    mycursor = mydb.cursor()

    # Consulta ao banco de dados para obter o produto que foi clicado
    produto = (f"SELECT preco, foto, descricao, categoria, cod_prod FROM tb_produto WHERE descricao = '{nome}'")

    mycursor.execute(produto)
    resultado = mycursor.fetchone()

    comentarioSelecionado = (f"SELECT * FROM tb_comentario c INNER JOIN tb_produto p ON p.cod_prod = c.cod_prod WHERE descricao = '{nome}' ;")

    mycursor.execute(comentarioSelecionado)
    comentarios = mycursor.fetchall()
    
    mydb.close()
    
    dicionario_produto ={
            "preco":resultado[0],
            "foto":resultado[1],
            "descricao":resultado[2],
            "categoria":resultado[3],
            "cod_prod":resultado[4]
    }

    lista_comentario = []
    for coment in comentarios:
        lista_comentario.append({
            "cpf_cliente":coment[0],
            "avaliacao":coment[1]
    })
    
    return render_template("sobre-produtos-raybelle.html", dicionario_produto = dicionario_produto, lista_comentario = lista_comentario)

# roteamento
@app.route("/carrinho", methods=["GET", "POST"])
def pagina_carrinhoDeCompras():
    btnCodProd = request.form['btnAdicionar']
    cpfCliente = session['usuario_logado']['cpf']

    # conectando o banco de dados
    mydb = Conexao.conectar()

    mycursor = mydb.cursor()

    carrinho = (f"INSERT INTO tb_carrinho (cpf_cliente, id_prod, quantidade) VALUES ('{cpfCliente}', '{btnCodProd}', 1)")

    mycursor.execute(carrinho)

    mydb.commit()

    mydb.close()

    return redirect('/')

@app.route("/api/carrinhoProdutos", methods=["GET"])
def pagina_carrinhoProdutos():

    # Conectar ao banco de dados para obter os itens do carrinho
    mydb = Conexao.conectar()
    mycursor = mydb.cursor()

    cpfCliente = session['usuario_logado']['cpf']

    mycursor.execute(f"SELECT p.descricao, p.preco FROM tb_produto p INNER JOIN tb_carrinho c ON p.cod_prod = c.id_prod WHERE cpf_cliente = '{cpfCliente}'")

    itens_carrinho = mycursor.fetchall()

    mydb.close()

    
    # Retorna os itens do carrinho como JSON
    return jsonify(itens_carrinho)

@app.route("/inserirProduto", methods=["GET","POST"])
def pagina_inserirProdutos():
    if request.method == 'GET':
        return render_template("inserir-produtos-raybelle.html")
    if request.method == 'POST':
        codProduto = request.form['codProduto']
        nomeProduto = request.form['nomeProduto']
        precoProduto = request.form['precoProduto']
        fotoProduto = request.form['fotoProduto']
        descricaoProduto = request.form['descricaoProduto']
        categoriaProduto= request.form['categoriaProduto']

        # Conectar ao banco de dados para obter os itens do carrinho
        mydb = Conexao.conectar()
        mycursor = mydb.cursor()

        inserir = (f"INSERT INTO tb_produto (cod_prod, nome_prod, preco, foto, descricao, categoria) VALUES ({codProduto}, {nomeProduto}, {precoProduto}, {fotoProduto}, {descricaoProduto}, {categoriaProduto})")

        mycursor.execute(inserir)

        mydb.commit()

        mydb.close()

        return redirect('/')

app.run(debug=True)