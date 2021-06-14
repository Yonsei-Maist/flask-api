from api.common.error.custom_exceptions import SampleTestError
from api.common.response.error_response_message import error_response_message


def error_handle(app):

    @app.errorhandler(Exception)
    def handle_exception(e):
        return error_response_message(str(e))

    # custom_error
    @app.errorhadler(SampleTestError)
    def handle_exception(e):
        return error_response_message({'message': e.message, 'errorMessage': e.error_message})
