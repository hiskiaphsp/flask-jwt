from flask import jsonify
import platform

def success_response(data=None, message=None, status=200):
    response = {
        "status": status,
        "message": message,
        "server": {
            "platform": platform.system(),
            "version": platform.version(),
        },
        "data": data
    }
    return jsonify(response), status

def error_response(message=None, error=None, status=400):
    response = {
        "status": status,
        "message": message,
        "server": {
            "platform": platform.system(),
            "version": platform.version(),
        },
        "error": error or "An error occurred"
    }
    return jsonify(response), status
