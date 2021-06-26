from flask import Flask
# from .calc import soma


def create_app():
    app = Flask(__name__)

    @app.get('/soma/<int:x>/<int:y>')
    def home(x, y):
        # return str(soma(x, y))
        return f'blah {x} e {y}'

    return app
