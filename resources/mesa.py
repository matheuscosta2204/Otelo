from flask_restful import Resource, reqparse
from models.mesa import MesaModel

class Mesa(Resource):

    parser = reqparse.RequestParser()
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

    def post(self, number):
        data = Mesa.parser.parse_args()

        if MesaModel.find_by_number(number):
            return {'message': "A table with number '{}' already exists.".format(number)}, 400

        mesa = MesaModel(number, data['nmb_places'], data['status'])
        try:
            mesa.save_to_db()
        except:
            return {"message": "An error occurred creating the table."}, 500

        return mesa.json(), 201

    def put(self, number):
        data = Mesa.parser.parse_args()

        item = MesaModel.find_by_number(number)
        if not item:
            return {'message': "A table with number '{}' not exists.".format(number)}, 404

        item.nmb_places = data['nmb_places']
        item.status = data['status']

        item.update_to_db()

        return {'message': "A table with number '{}' ".format(item.json())}, 201

    def delete(self, number):
        item = MesaModel.find_by_number(number)
        if not item:
            return {'message': "A table with number '{}' does not exists".format(number)}, 404

        item.delete_from_db()

        return {'message': 'Item deleted'}, 200

class MesaDisponible(Resource):
    def get(self):
        return MesaModel.find_all_mesas_disponible()
