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

#    def post(self, number, nmb_places, status):
#        if MesaModel.find_by_number(number):
#            return {'message': "A table with name '{}' already exists.".format(number)}, 400
#
#        mesa = MesaModel(number, nmb_places, status)
#        try:
#            mesa.save_to_db()
#        except:
#            return {"message": "An error occurred creating the table."}, 500
#
#        return mesa.json(), 201

#class MesaCountDisponible(Resource):
    #def get(self):
        #return {'mesas': [{'nmb_places': mesa.nmb_places, 'number_disponible': mesa.Disponible} for mesa in MesaModel.count_disponible()]}
