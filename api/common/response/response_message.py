from api.config.config import Config

success = {
    "version": Config.VERSION,
    "result": "success"
}

def response_message(data=None):
    return dict(success, **{"data": data}),200