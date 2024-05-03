from flask import Flask , render_template, request, redirect, session, jsonify

#app é o servidor
#criei o objeto app usando a classe Flask
app = Flask(__name__)
app.secret_key = 'raybelle'

#roteamento da página
@app.route("/")
def pagina_inicial():
    return render_template("raybelle.html")

@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro-raybelle.html")

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

@app.route("/todos_prod")
def pagina_todos_prod():
    return render_template("todosProd-raybelle.html")

app.run(debug=True)