import flask
from shop_app.models import *

def render_cart():
    cookies = flask.request.cookies.get('list_products')

    list_products = []
    if cookies != None:
        cookies = cookies.split("|")
        for id in cookies:
            if id != '':
                product = Product.query.get(ident = id)
                if [product, cookies.count(id)] not in list_products:
                    list_products.append([product, cookies.count(id)])
            
    return flask.render_template('cart.html', list_products = list_products)

def delete_product():
    cookies = flask.request.cookies.get(key = "list_products")
    if flask.request.method == "POST":
        id = flask.request.form.get("id")
        response = flask.make_response(flask.redirect("/cart"))
        response.set_cookie("list_products", cookies.replace(f"{id}|", ""))
        
    return response