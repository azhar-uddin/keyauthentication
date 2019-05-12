from functools import wraps
from flask import request, abort, current_app as app

def require_appkey(secure_funtion):
    @wraps(secure_funtion)
    
    def verify_appkey(*args, **kwargs):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == app.config['APP_KEY']:
            return secure_funtion(*args, **kwargs)
        else:
            abort(401, 'Unauthorized')
    return verify_appkey