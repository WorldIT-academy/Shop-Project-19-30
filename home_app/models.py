import flask_login
from project.db import *

# flask_login.UserMixin - Клас который должна наследовать модель пользователя
# Сессия - хранит то какой я пользователь, в зашифрованом виде. Находиться в cookies файлах бразуре
class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String)
    password = DATABASE.Column(DATABASE.String)
    is_admin = DATABASE.Column(DATABASE.Boolean)
