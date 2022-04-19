import hashlib

from app import db

from app.views import blueprint

from flask import jsonify, request, abort

from app.models import User, Role, Session

@blueprint.route('/login', methods=['POST'])
def login():
    def _validate(request) -> bool:
        if 'username' not in request:
            return False       
        if 'password' not in request:
            return False
        return True

    if not request.jsom:
        abort(400, 'Request is not JSON')
    if not _validate(request.json):
        abort(400, 'One or more fields are required.')

    _username = request.json['username']
    _password = (
        haslib.md5(request.json['password'].encode()).hexdigest()
    )

    user = (
        User.query.filter(
            (
                db.func.lower(User.username) == _username.lower()
            ) and (
                User.password == _password
            )
        ).first()
    )

    if not user:
        abort(404, "User does not exist")

    session = (
        Session.query.filter_by(user_id=user_id).first()
    )

    if session:
        db.session.delete(session)
        db.session.commit()

    # If exist (User), make session
    new_session = Session(
        user_id=user.id
    )

    db.session.add(new_session)
    db.session.commit()

    return jsonify(new_session.serialize()), 201

# http://127.0.0.1:5000/vandyck/hi
@blueprint.route('/users', methods=['GET'])
def get_users():
    users = [
        user.serialize()
        for user in User.query.all()
    ]

    """
        {
            {
                'id': 1,
                'username': xxx
            },
            {
                'id': 1,
                'username': xxx
            }
        }
    """

    return jsonify(users)

# POST /users
@blueprint.route('/users', methods=['POST'])
def add_user():
    if not request.json:
        abort(404, "Role is not found")
    
    def _validate(request) -> bool:
        if 'username' not in request:
            return False
        if 'password' not in request:
            return False
        if 'role' not in request or not isinstance(request['role'], str):
            return False
        return True

    if not _validate(request.json):
        abort(400, "One or more fileds are required")
    
    _username = request.json['username']
    _password = request.json['password']
    _role = request.json['role']

    role = Role.query.filter(
        db.func.lower(
            Role.name
        ) == _role.lower()
    ).first()

    if not role:
        print("Role is not found")
        abort(404, 'Role is not found') # Role not found
    
    # Validate User
    user = User.query.filter(
        db.func.lower(User.username) == _username.lower()
    ).first()

    if user:
        abort(409, 'User exists') # User exists
    
    new_user = User (
        username = _username,
        password = hashlib.md5(_password.encode()).hexdigest(),
        role_id = role.id
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.serialize()), 201