from .urls import *
from .db import *
from .loadenv import *
from .settings import *
from .login_manager import *

from home_app.models import User


from home_app.apps import *
from shop_app.apps import *
from cart_app.apps import *


project.register_blueprint( blueprint = home)
project.register_blueprint( blueprint = registration)
project.register_blueprint( blueprint = authorization)
project.register_blueprint( blueprint = shop)
project.register_blueprint( blueprint= cart)