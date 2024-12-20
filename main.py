from flask import Flask, render_template, redirect, url_for, flash, request
from models import db, Clientes

app = Flask(__name__)
app.secret_key = 'page_clone'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/clientes.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/tratamentos')
def tratamentos():
    return render_template('tratamentos.html')

@app.route('/botox')
def botox():
    return render_template('botox.html')

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
    
    
if __name__ == '__main__':
    app.run(debug=True)