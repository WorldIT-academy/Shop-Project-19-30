import home_app, shop_app, cart_app

home_app.home.add_url_rule("/", view_func = home_app.render_home)
home_app.registration.add_url_rule("/reg/", view_func = home_app.render_register, methods = ["GET", "POST"])
home_app.authorization.add_url_rule("/auth/", view_func = home_app.render_authorization, methods = ["GET", "POST"])
home_app.home.add_url_rule("/logout/", view_func = home_app.render_logout)

shop_app.shop.add_url_rule('/shop/', view_func = shop_app.render_home, methods = ["GET", "POST"])
shop_app.shop.add_url_rule('/delete_product/', view_func = shop_app.delete_product, methods = ["GET", "POST"])
shop_app.shop.add_url_rule('/buy_product/', view_func = shop_app.add_product, methods = ["GET", "POST"])
cart_app.cart.add_url_rule('/cart/', view_func = cart_app.render_cart, methods = ["GET", "POST"])
cart_app.cart.add_url_rule('/delete', view_func = cart_app.delete_product, methods = ["GET", "POST"])