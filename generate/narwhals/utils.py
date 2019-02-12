
def success_response(data):
    """
    {  
        success: [ true ],
        message: [ null ],
        data: [ data ],
    }
    """
    response = {}
    response["data"] = data
    response["success"] = "true"
    response["message"] = "null"

    return response

def error_response(error):
    """
    {  
        success: [ false ],
        message: [ "error msg" ],
    }
    """
    response = {}
    response["success"] = "false"
    response["message"] = error

    return response
