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
    message = error
    if isinstance(error, dict):
        message = ''
        for key, value in error.iteritems():
            if isinstance(value, list):
                for item_value in value:
                    message += '%s ' % item_value
            else:
                message += '%s , ' % value
    response["message"] = message

    return response
