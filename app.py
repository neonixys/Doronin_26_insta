import os

from flask import Flask
from api.api import api_blueprint
from posts.views import posts_blueprint

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Регистрируем блюпринты
app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(_):
    return "Страница не найдена"


@app.errorhandler(500)
def page_not_found(_):
    return "На сервере что то пошло не так"


if __name__ == "__main__":
    app.run()
