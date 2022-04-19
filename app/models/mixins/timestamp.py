import datetime

from apu_cas import get_user_cas_attributes

from app import db

def get_current_samaccountname():
    if get_user_cas_attributes():
        return get_user_cas_attributes().sam_account_name[0]
    
    return "SUPERUSER"

class CreateTimestampMixin(object):
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now
    )
    accountname = db.Column(
        db.String(64),
        default=get_current_samaccountname
    )
