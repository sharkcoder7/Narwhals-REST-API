from rest_framework.views import exception_handler

from utils.helpers import error_response

def auth_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Customized for Android
    if response is not None:
        response.data["success"] = False
        response.data["message"] = response.data["detail"]
        del response.data["detail"]

    return response
