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
    response["success"] = True
    response["message"] = None

    return response

def error_response(error):
    """
    {  
        success: [ false ],
        message: [ "error msg" ],
    }
    """
    response = {}
    response["success"] = False
    response["message"] = error

    return response
