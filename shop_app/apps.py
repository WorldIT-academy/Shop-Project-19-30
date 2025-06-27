import flask 

shop = flask.Blueprint(
    template_folder="templates",
    name = "shop",
    import_name = "shop_app",
    static_folder= 'static',
    static_url_path= '/static_shop'
)