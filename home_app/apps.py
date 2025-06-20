import flask

home = flask.Blueprint(
    name = 'home',
    import_name = 'home_app',
    template_folder = 'templates',
    static_folder = 'static',
    static_url_path = '/static_home/'
)

registration = flask.Blueprint(
    name = 'registration',
    import_name = 'home_app',
    template_folder = 'templates',
    static_folder = 'static',
    static_url_path = '/static_registration/'
)
authorization = flask.Blueprint(
    name = 'authorization',
    import_name = 'home_app',
    template_folder = 'templates',
    static_folder = 'static',
    static_url_path = '/static_authorization/'
)
