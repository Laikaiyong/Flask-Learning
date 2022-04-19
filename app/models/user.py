from app import db

from app.models.mixins import CreateTimestampMixin

class Role(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        nullable=False
    )

    def serialize(self, full=False):
        serialized = {
            "id": self.id,
            "name": self.name
        }

        if full:
            serialized['users'] = [
                user.serialize()
                for user in self.users
            ]

        return serialized

class User(db.Model, CreateTimestampMixin):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        nullable=False
    )
    password = db.Column(
        db.String(64),
        nullable=False
    )
    role_id = db.Column(
        db.Integer,
        db.ForeignKey("role.id"),
        nullable=False
    )
    role = db.relationship(
        'Role', 
        backref='users'
    )
    session = db.relationship('Session')

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role.serialize()
        }

    
