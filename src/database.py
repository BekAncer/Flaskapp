from models import db, Sneaker
import os
from werkzeug.utils import secure_filename


def get_catalog():
    result = db.session.execute(db.select(Sneaker).order_by(Sneaker.name)).scalars()
    return result


def add_to_catalog(request):
    from app import app
    file = request.files['image']
    filename = secure_filename(file.filename)
    sneaker = Sneaker(
        name=request.form["name"],
        price=request.form["price"],
        imgsrc=filename
    )
    db.session.add(sneaker)
    db.session.commit()
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


def delete_from_catalog_with_id(sneaker_id):
    sneaker = Sneaker.query.filter_by(id=sneaker_id).first()
    db.session.delete(sneaker)
    db.session.commit()
