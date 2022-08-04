from flask import Flask, render_template


def create_app():

    app = Flask(__name__)
    register_error_pages(app)


    return app


def register_error_pages(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404