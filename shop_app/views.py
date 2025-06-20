import flask, flask_login, os
from .models import *

def render_home():
    products = Product.query.all()
    is_admin = False
    if flask_login.current_user.is_authenticated and flask_login.current_user.is_admin:
        is_admin = True
        if flask.request.method == "POST":
            product = Product(
                name = flask.request.form["name"],
                price = flask.request.form["price"],
                description = flask.request.form["description"],
                count = flask.request.form["count"],
                discount = flask.request.form["discount"]
            )
            DATABASE.session.add(product)
            DATABASE.session.commit()
            image = flask.request.files["image"]
            image.save(
                dst = os.path.abspath(os.path.join(__file__,  '..', "static", "images", "products", f'{flask.request.form["name"]}.png'))
            )
            # flask.request.files - отримує файли з форми

    # Для того щоб передати дані на сторінку у функцію render_template, потрібно вказати ці дані
    # hr - тег, лінія розділення 
    return flask.render_template("shop.html", is_admin = is_admin, products = products)
    

def delete_product():
    if flask_login.current_user.is_authenticated and flask_login.current_user.is_admin:
        id = flask.request.args["id"]
        product = Product.query.get(id)
        # DATABASE.session.delete - видаляє запис з бази даних
        DATABASE.session.delete(product)
        DATABASE.session.commit()
    return flask.redirect("/shop/")

def add_product():
    response = flask.make_response(flask.redirect("/shop/"))
    id = flask.request.args['id']
    cookies = flask.request.cookies.get("list_products")
    if cookies == None:
        response.set_cookie("list_products", id)
    else:
        cookies += "|" + id
        response.set_cookie("list_products", cookies)
    return response