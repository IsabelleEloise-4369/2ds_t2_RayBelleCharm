from flask import Flask , render_template, request, redirect, session, jsonify
from usuario import Usuario

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
                                         'senha':usuario.senha}
            return redirect('/comentario')
        else:
            session.clear()
            return 'Email ou senha incorretos.'

#roteamento da página comentário
@app.route("/comentario", methods=["GET", "POST"])
#função da página de comentário
def pagina_comentario():
    return render_template("comentario-raybelle.html")

#roteamento da página de produtos ouro
@app.route("/ouro")
#função da página de produtos apenas de ouro
def pagina_ouro():
    return render_template("ouro-raybelle.html")

#roteamento da página de produtos prata
@app.route("/prata")
#função da página de produtos apenas de prata
def pagina_prata():
    return render_template("prata-raybelle.html")

app.run(debug=True)