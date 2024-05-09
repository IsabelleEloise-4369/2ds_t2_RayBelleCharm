from flask import Flask , render_template, request, redirect, session, jsonify
from usuario import Usuario

#app é o servidor
#criei o objeto app usando a classe Flask
app = Flask(__name__)
app.secret_key = 'raybelle'

#roteamento da página
@app.route("/")
def pagina_inicial():
    return render_template("raybelle.html")

@app.route("/cadastro", methods=["GET", "POST"])
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


@app.route("/login")
def pagina_logn():
    return render_template("login-raybelle.html")

@app.route("/comentario")
def pagina_comentaio():
    return render_template("comentario-raybelle.html")

@app.route("/ouro")
def pagina_ouro():
    return render_template("ouro-raybelle.html")

@app.route("/prata")
def pagina_prata():
    return render_template("prata-raybelle.html")

app.run(debug=True)