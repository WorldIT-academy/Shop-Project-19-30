import flask, flask_login
from .models import *
from project.db import *

def render_home():
    # flask_login.current_user - Хранит акаунт пользователя, или аноним
    # flask_login.current_user.is_authenticated - Хранит находиться ли пользователь в акаунте
    # flask_login.logout_user() - Функция выхода из акаунта
    return flask.render_template("home.html")
    
def render_register():
    if flask.request.method == "POST":
        name = flask.request.form["username"]
        password = flask.request.form["password"]
        user = User(
            name = name,
            password = password,
        )
        DATABASE.session.add(user)
        DATABASE.session.commit()
        

    return flask.render_template("register.html")
    
def render_authorization():
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        password = flask.request.form["password"]
        # Модель.query.all() - получает все записи из модели
        list_user = User.query.all()
        for user in list_user:
            if user.name == name and user.password == password:
                flask_login.login_user(user)

    return flask.render_template("auth.html")


def render_logout():
    if flask_login.current_user.is_authenticated:
        flask_login.logout_user()
    # flask.redirect - перенаправляет пользователя по указанной ссылке
    return flask.redirect('/')
    
    


