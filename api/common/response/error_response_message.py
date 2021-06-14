from api.config.config import Config

fail = {
    "version": Config.VERSION,
    "result": "fail"
}


def error_response_message(message):
    return dict(fail, **{"message": message}), 500
