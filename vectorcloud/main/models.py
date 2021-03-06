from vectorcloud import db


class Files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    path = db.Column(db.String())
    external_path = db.Column(db.String())
    cache = db.Column(db.String())
    folder = db.Column(db.String())


class Logbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    info = db.Column(db.String())
    dt = db.Column(db.String())
    log_type = db.Column(db.String())
    vector_id = db.Column(db.Integer, db.ForeignKey("vectors.id"))


class Vectors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String())
    cert_file = db.Column(db.String())
    ip = db.Column(db.String())
    name = db.Column(db.String())
    guid = db.Column(db.String())
    custom_name = db.Column(db.String())
    description = db.Column(db.String())
    logbook_items = db.relationship(
        "Logbook", backref="vector", order_by="desc(Logbook.dt)"
    )


class Repositories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    name = db.Column(db.String())
    fp = db.Column(db.String())


db.create_all()
db.session.commit()
