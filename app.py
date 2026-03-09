from datetime import datetime

from flask import Flask, render_template, url_for, flash, request, redirect
from database import db_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha'

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # pega o campo do formulario
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')

        '''
        if not email or not senha:
            flash('Por favor informe os campos!', 'alert-danger')
            return render_template('login.html')
            '''

        if email and senha:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
            if resultado_email:
                if resultado_email.check_password(senha):
                    # Realiza a autenticação
                    login_user(resultado_email)
                    flash(f'Login realizado com sucesso!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Senha incorreta!', 'alert-danger')
                    return redirect(url_for('login'))
            else:
                flash(f'Usuario não encontrado!', 'alert-danger')
                return redirect(url_for('login'))
        else:
            flash(f'Preencha os campos', 'alert-danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/funcionarios', methods=['GET', 'POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        if (request.form['form-nome'] and request.form['form-data-nasc'] and request.form['form-cpf'] and request.form['form-email'] and
                request.form['form-senha'] and request.form['form-cargo'] and request.form['form-salario']):
            nome = request.form['form-nome']
            data_nasc = datetime.strptime(request.form['form-data-nasc'], "%Y-%m-%d")
            cpf = request.form['form-cpf']
            email = request.form['form-email']
            senha = request.form['form-senha']
            cargo = request.form['form-cargo']
            salario = float(request.form['form-salario'])


            user_email = select(Funcionario).where(Funcionario.email == email)
            user_email = db_session.execute(user_email).scalars().one_or_none()

            if user_email:
                flash("Usuário ja existe", 'alert-danger')
            else:
                funcionario = Funcionario(nome=nome, data_nascimento=data_nasc,cpf=cpf ,email=email, senha=senha, cargo=cargo, salario=salario)
                funcionario.set_password(senha)
                db_session.add(funcionario)
                db_session.commit()
                db_session.close()
        else:
            flash("Preencha todos os campos", 'alert-danger')
        return redirect(url_for('funcionarios'))
    return render_template("funcionarios.html")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/calculos')
def calculos():
    return render_template("calculos.html")


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")


@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/lista_funcionarios')
@login_required
def funcionarios():
    funcionarios_sql = select(Funcionario)
    funcionarios_resultado = db_session.execute(funcionarios_sql).scalars().all()
    print(funcionarios_resultado)

    return render_template("funcionarios.html", lista_funcionarios=funcionarios_resultado)


@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("Soma realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            # Passo 1: Emitir a mensagem e a catedoria do flash
            flash("Preencha o campo para realizar a soma", 'alert-danger')

    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtracao = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)

    return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicacao = n1 * n2
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicacao=multiplicacao)

    return render_template("operacoes.html")


@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            divisao = n1 / n2
            return render_template("operacoes.html", n1=n1, n2=n2, divisao=divisao)

    return render_template("operacoes.html")


@app.route('/area_triangulo', methods=['GET', 'POST'])
def area_triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            triangulo = n1 * n2 / 2
            return render_template('geometria.html', n1=n1, n2=n2, triangulo=triangulo)
    return render_template("geometria.html")


@app.route('/area_circulo', methods=['GET', 'POST'])
def area_circulo():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            circulo = n1 * n1 * 3.14
            return render_template('geometria.html', n1=n1, circulo=circulo)


# TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)
