from app import db

# from apu_cas.user_role import UserRole
# from apu_cas import require_service_ticket, get_user_cas_attributes

from app.helpers import require_api_token

from flask import Blueprint, jsonify

from app.models.user import User, Role

blueprint = Blueprint('views', __name__)

# Route Declaration
from app.views import user
from app.views import role

@blueprint.route('/test')
# @require_service_ticket(
#     deny_for_roles=[
#         UserRole.STUDENT
#     ],
#     restricted_to_roles=[
#         UserRole.CTI
#     ]
# )
def test():
    result = (
        db
        .session
        .query(
            User,
            Role
        )
        .select_from(User)
        .join(
            Role.id == User.role_id
        )
        .with_entities(
            User.username,
            Role.name
        )
        .all()
    )

    # Normalizing data
    (
        users, 
        roles 
    ) = list(zip(*result))

    # Exchange tuple to list
    users = list(users)
    roles = list(roles)

    return jsonify(
        {
            'users': users,
            'roles': roles
        }
    )

@blueprint.route('/')
@require_api_token
def index(*args, **kwargs):
    _user = kwargs['user']
    return jsonify(_user.serialize())
