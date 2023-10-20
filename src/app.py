from flask import Flask, render_template, request
from models import db
from database import get_catalog, add_to_catalog, delete_from_catalog_with_id
from config import DB_URI

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db.init_app(app)

menu = [
    {"name": "Добавить", "url": "/catalog-change"},
    {"name": "Убрать", "url": "/catalog-delete"},
    {"name": "Каталог", "url": "/catalog"},
    {"name": "Контакты", "url": "/contacts"},
]


@app.route("/")
@app.route("/contacts")
def contacts():
    return render_template('contacts.html', Menu=menu)


@app.route("/catalog-change", methods=["POST", "GET"])
def catalog_change():
    if request.method == "POST":
        add_to_catalog(request)
    return render_template('catalog-change.html', Menu=menu)


@app.route("/catalog-delete", methods=["POST", "GET"])
def delete_sneaker():
    if request.method == "POST":
        delete_from_catalog_with_id(request.form['sneaker-id'])
    sneakers = get_catalog()
    return render_template('catalog-delete.html', Sneakers=sneakers, Menu=menu)


@app.route("/catalog")
def about():
    sneakers = get_catalog()
    return render_template('catalog.html', Sneakers=sneakers, Menu=menu)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0', port=5001
        # gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
    )
