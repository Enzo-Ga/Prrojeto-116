# importando os módulos da biblioteca flask
from flask import Flask, render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'


@app.route("/")
def home():

    nome = "Enzo Gabriel"  # escreva seu nome
    idade = "18"  # escreva sua idade

    return render_template('index.html', nome=nome, idade=idade)

# defina a rota para a página do pai


@app.route('/pai')
def father():

    nome = "Marcelo"
    idade = "40"

    return render_template('pai.html', nome=nome, idade=idade)

# defina a rota para a página da mãe


@app.route('/mae')
def mother():

    nome = "Luciana"
    idade = "37"

    return render_template('mae.html', nome=nome, idade=idade)

# defina a rota para a página do amigo


@app.route('/irmao1')
def brother1():

    nome = "Giovanni"
    idade = "22"

    return render_template('irmao1.html', nome=nome, idade=idade)


# adicione outras rotas, se você quiser
@app.route('/irmao2')
def brother2():

    nome = "Guilherme"
    idade = "20"

    return render_template('irmao2.html', nome=nome, idade=idade)


# execute o arquivo
if __name__ == '__main__':
    app.run(debug=True)
