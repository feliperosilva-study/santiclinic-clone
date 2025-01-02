from flask import Flask, render_template, redirect, url_for, flash, request
from models import db, Clientes

app = Flask(__name__)
app.secret_key = 'page_clone'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/clientes.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/tratamentos')
def tratamentos():
    return render_template('tratamentos.html')

@app.route('/botox')
def botox():
    return render_template('botox.html')

@app.route('/acido')
def acido():
    return render_template('acido.html')

@app.route('/harmonizacao')
def harmonizacao():
    return render_template('harmonizacao.html')

@app.route('/bio')
def bio():
    return render_template('bio-estimulador.html')

@app.route('/peeling')
def peeling():
    return render_template('peeling.html')

@app.route('/lemon')
def lemon():
    return render_template('lemon.html')

@app.route('/mesoterapia')
def mesoterapia():
    return render_template('mesoterapia.html')

@app.route('/collagen')
def collagen():
    return render_template('collagen.html')

@app.route('/remocao')
def remocao():
    return render_template('remocao.html')

@app.route('/analises')
def analises():
    return render_template('analises.html')

@app.route ('/form-tratamento', methods=['POST'])
def formulario():

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telemovel = request.form.get('telemovel')
        consulta = request.form.get('consulta')
        duvida = request.form.get('duvida')

        if nome == '' or email == '' or telemovel == '':
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')
            return redirect(url_for('botox', _anchor='form-tratamento'))

        if not all(c.isalpha() or c.isspace() for c in nome):
            flash('Caracteres Inválidos. Campo NOME aceita apenas letras e espaços', 'error-nome')
            return redirect(url_for('botox', _anchor='form-tratamento'))

        if not telemovel.isdigit():
            flash('Caracteres Inválidos. Campo TELEMÓVEL aceita apenas números', 'error-tel')
            return redirect(url_for('botox', _anchor='form-tratamento'))

        novo_cliente = Clientes (
            nome = nome,
            email = email,
            telemovel = telemovel,
            consulta = consulta,
            duvida = duvida
        )

        db.session.add(novo_cliente)
        db.session.commit()

        flash('Formulário enviado com sucesso', 'success')
        return redirect(url_for('botox', _anchor='form-tratamento'))
    
@app.route('/contactos')
def contactos():
    return render_template('contactos.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)