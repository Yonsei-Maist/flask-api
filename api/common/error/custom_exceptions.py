class CustomSampleError(Exception):
    def __init__(self, status_code, message, error_message):
        self.status_code = status_code
        self.message = message
        self.error_message = error_message


class SampleTestError(CustomSampleError):
    def __init__(self, error_message):
        status_code = 400
        message = '에러메시지'
        error_message = error_message
        super().__init__(status_code, message, error_message)