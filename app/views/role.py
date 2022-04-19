from app import db

from app.views import blueprint

from flask import jsonify, request, abort

from app.models import Role

# http://127.0.0.1:5000/vandyck/hi
@blueprint.route('/roles', methods=['GET'])
def get_role():
    roles = [
        role.serialize()
        for role in Role.query.all()
    ]

    return jsonify(roles)

@blueprint.route('/roles', methods=['POST'])
def add_role():
    if not request.json:
        abort(400)
    
    def _validate(request) -> bool:
        if 'name' not in request:
            return False
        return True

    if not _validate(request.json):
        abort(400)
    
    _name = request.json['name']

    # Check role exists
    has_role = (
        Role.query.filter(
            db.func.lower(Role.name) == _name.lower()
        ).first()
    )

    if not has_role:
        # Add role through Model
        new_role = Role(
            name=_name
        )
        db.session.add(new_role)
        db.session.commit()

        return jsonify(new_role.serialize()), 201
    else:
        print("Role Exists")
        abort(400)
