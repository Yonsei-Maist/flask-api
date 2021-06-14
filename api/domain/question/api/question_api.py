from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from lib.jwt import create_jwt_token, get_claims

from api.common.response.response_message import response_message
from api.domain.question.service.question_service import QuestionService

bp = Blueprint('question', __name__, url_prefix='/question')
question_service = QuestionService()


class QuestionApi:

    @jwt_required()  # jwt check
    @cross_origin()  # cross origin check
    @bp.route('/', methods=['GET'])
    def question_list(*args):
        claims = get_claims()  # get saved data in token
        return response_message(question_service.question_list())

    @cross_origin()
    @bp.route('/', methods=['POST'])
    def create(*args):
        question_service.create(request.get_json())
        return response_message()

    @cross_origin()
    @bp.route('/<int:question_id>', methods=['PUT'])
    def update(*args, question_id):
        question_service.update(question_id, request.get_json())
        return response_message()

    @cross_origin()
    @bp.route('/<int:question_id>', methods=['DELETE'])
    def delete(*args, question_id):
        question_service.delete(question_id)
        return response_message()

    @cross_origin()
    @bp.route('/login', methods=['POST'])
    def login(*args):
        json = request.get_json()
        id = json['id']

        return create_jwt_token(id)  # create token
