from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Category import CategoryResource
from Model import *
from resources.Comment import CommentResource
#from resources import *


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')

api.add_resource(CategoryResource, '/category', endpoint = 'Category')
api.add_resource(CommentResource, '/comment')
