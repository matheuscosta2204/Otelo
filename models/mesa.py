from db import db

class MesaModel(db.Model):
    __tablename__ = 'mesas'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    nmb_places = db.Column(db.Integer)
    status = db.Column(db.String(80))

    def __init__(self, number, nmb_places, status):
        self.number = number
        self.nmb_places = nmb_places
        self.status = status

    def json(self):
        return {'number': self.number, 'nmb_places': self.nmb_places, 'status': self.status}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self):
        db.session.delete(self)
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_number(cls, number):
        return cls.query.filter_by(number=number).first()

    @classmethod
    def find_all_mesas_disponible(cls):
        qry = cls.query.filter_by(status='livre').all()
        return {"Mesas": [{'disponible': cls.query.filter_by(nmb_places=mesa.nmb_places).count(), 'nmb_places': mesa.nmb_places} for mesa in qry]}
