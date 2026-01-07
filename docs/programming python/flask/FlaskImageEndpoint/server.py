from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Image API', description='A simple Image API')

ns = api.namespace('images', description='Image operations')

image_model = api.model('Image', {
    'image': fields.String(required=True, description='The image in base64 format')
})

images = {'1':'base64encodeddefaultimage'}

@ns.route('/<string:image_id>')
@ns.response(404, 'Image not found')
@ns.param('image_id', 'The image identifier')
class Image(Resource):
    @ns.doc('get_image')
    @ns.response(200, 'Success')
    def get(self, image_id):
        '''Fetch an image given its identifier'''
        if image_id not in images:
            api.abort(404, "Image {} doesn't exist".format(image_id))
        return images[image_id]

    @ns.doc('update_image')
    @ns.expect(image_model)
    @ns.response(204, 'Image updated successfully')
    def put(self, image_id):
        '''Update an image given its identifier'''
        if image_id not in images:
            api.abort(404, "Image {} doesn't exist".format(image_id))
        image_data = request.json
        images[image_id] = image_data
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
