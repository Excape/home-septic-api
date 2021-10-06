from flask_restplus import Resource, fields, Namespace, reqparse
from flask import current_app, request
from ..homecanary.homecanaryapi import HomeCanaryApi
from . import mapper, auth

namespace = Namespace('sewer', 'Endpoint to get the type of sewer for a property')

sewer_response_model = namespace.model('SewerResponse', {
    'address': fields.String(
        readonly=True,
        description='Requested Address'
    ),
    'zipcode': fields.String(
        readonly=True,
        description='Requested Zip code'
    ),
    'sewertype': fields.String(
        readonly=True,
        enum=['None', 'Yes', 'Storm', 'Municipal', 'Septic']
    )
})

parser = reqparse.RequestParser()
parser.add_argument('address', type=str, required=True, help='Address of the property')
parser.add_argument('zipcode', type=str, required=True, help='Zip code of the property')

@namespace.route('')
class HomeSepticResource(Resource):

    @namespace.marshal_list_with(sewer_response_model)
    @namespace.expect(parser)
    @namespace.response(400, 'missing arguments')
    @namespace.response(401, 'not authorized')
    @namespace.response(404, 'requested property not found by API')
    @namespace.response(500, 'internal API error')
    @namespace.doc(security='apikey')
    def get(self):
        if not auth.is_authorized(request):
            namespace.abort(401, 'Unauthorized. Please provide an API key in the X-API-KEY header')
            return
        
        args = request.args
        if ('address' not in args):
            namespace.abort(400, 'Missing argument address')
            return
        if ('zipcode' not in args):
            namespace.abort(400, 'Missing argument zipcode')
            return

        requested_address = args.get('address')
        requested_zip_code = args.get('zipcode')

        api = HomeCanaryApi(current_app.config)
        
        propertySewer = api.get_propertysewer(requested_address, requested_zip_code)

        if propertySewer is None:
            namespace.abort(404, 'Requested property was not found')
            return

        return mapper.map_propertysewer_to_rest_response(propertySewer)
