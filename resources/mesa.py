from flask_restful import Resource, reqparse
from models.mesa import MesaModel
class Mesa(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('number',
        type=int,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('nmb_places',
        type=int,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('status',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

class MesaCountDisponible(Resource):
    def get(self):
        return {'mesas': [{'nmb_places': mesa.nmb_places, 'number_disponible': mesa.Disponible} for mesa in MesaModel.count_disponible()]}
