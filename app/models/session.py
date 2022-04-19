import secrets

from app import db

class Session(db.Model):
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        primary_key = True,
        autoincrement=False
    )
    token = db.Column(
        db.String(256),
        nullable=False,
        default=secrets.token_urlsafe(16)
    )

    user = db.relationship('User')

    __table_args__ = (
        db.UniqueConstraint(
            'user_id', 
            'token', 
            name='unique_user_token'
        ),
        
    )

    def serialize(self):
        return {
            "token": self.token
        }
