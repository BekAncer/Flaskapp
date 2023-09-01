from flask import Flask, render_template, request
from models import DB_URI, Sneaker, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db.init_app(app)


# https://restfulapi.net/resource-naming/
menu = [
    {"name": "Добавить", "url": "/CatalogChange"},
    {"name": "Убрать", "url": "/CatalogDelete"},
    {"name": "Каталог", "url": "/SneakerCatalog"},
    {"name": "Контакты", "url": "/Contacts"},
]


@app.route("/")
@app.route("/contacts")
def contacts():
    return render_template('contacts.html', Menu=menu)


@app.route("/catalog-change", methods=["POST", "GET"])
def catalog_change():
    if request.method == "POST":
        sneaker = Sneaker(
            name=request.form["name"],
            price=request.form["price"],
            imgsrc=request.form["imgsrc"]
        )
        db.session.add(sneaker)
        db.session.commit()
    return render_template('catalog-change.html', Menu=menu)


@app.route("/catalog-delete", methods=["POST", "GET"])
def delete_sneaker():
    if request.method == "POST":
        snkr = Sneaker.query.filter_by(name=request.form['name']).first()
        if snkr:
            db.session.delete(snkr)
            db.session.commit()
    return render_template('catalog-delete.html', Menu=menu)


@app.route("/catalog")
def about():
    # разделить работу с БД и эндпоинты
    Sneakers = db.session.execute(db.select(Sneaker).order_by(Sneaker.name)).scalars()
    return render_template('catalog.html', Sneakers=Sneakers, Menu=menu)


if __name__ == '__main__':
    # регулировать через переменные среды
    # обернуть в gunicorn/uvicorn
    app.run(
        host='0.0.0.0', port='5001'
    )
