from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('portfolio', '/portfolio')
    config.add_route('about', '/about')
    config.add_route('contact', '/contact')
    config.add_route('imager', '/imager')
    config.add_route('nighttime', '/nighttime')
    config.add_route('gameini', '/gameini')
    config.add_route('decodaquote', '/decodaquote')
    config.add_route('tasktrapper', '/tasktrapper')
    config.add_route('echelonjs', '/echelonjs')
    config.add_route('hangman', '/hangman')
    config.scan()
    return config.make_wsgi_app()
