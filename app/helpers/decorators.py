import functools

from flask import request, abort

from app.models import Session

def require_api_token(f):
    @functools.wraps(f)
    def require_api_token_wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(400, "Session Token not found.")

        # Get header value
        _token = request.headers.get('Authorization') 
        
        session = (
            Session.query.filter_by(
                token=_token.first()
            )
        )

        if not session:
            abort(401, "Unauthorized.")

        kwargs['user'] = session.user

        return f(*args, **kwargs)
    return require_api_token_wrapper
