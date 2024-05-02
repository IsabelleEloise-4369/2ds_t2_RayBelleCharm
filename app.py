from flask import Flask , render_template, request, redirect, session, jsonify

#app é o servidor
#criei o objeto app usando a classe Flask
app = Flask(__name__)
app.secret_key = 'raybelle'

#roteamento da página
@app.route("/")
def pagina_inicial():
    return render_template("raybelle.html")

app.run(debug=True)