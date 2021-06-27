"""Cria o factory da aplicação."""

from flask import Flask


def create_app():
    """Cria a aplicação."""
    app = Flask(__name__)

    @app.get('/soma/<int:x>/<int:y>')
    def home(x, y):
        # return str(soma(x, y))
        return f'blah {x} e {y}'

    return app
