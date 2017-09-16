from db import db
from SQLAlchemy import func

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

    @classmethod
    def find_by_number(cls, number):
        return cls.query.filter_by(number=number).first()

    def find_all_mesas_disponible():
        return cls.query.filter_by(staus="livre").all().group_by(number)
