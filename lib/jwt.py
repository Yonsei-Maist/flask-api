from flask_jwt_extended import create_access_token, get_jwt
from api import jwt


@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    """
    some saved data in token
    :param identity: identity from token
    :return: data to save token
    """
    return {
        'id': identity,
    }


def create_jwt_token(identity):
    """
    create token using identity
    :param identity: identity data that save to token
    :return: access token
    """
    return create_access_token(identity=identity)


def get_claims():
    return get_jwt()
