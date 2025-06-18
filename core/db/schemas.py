from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, EXCLUDE

ma = Marshmallow()

class UserSchema(ma.Schema):
    
    class Meta:
        unknown = EXCLUDE # makes sure unknown fields in the request aren't added to the db

    id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=3, max=100))
    email = fields.Email(required=True, validate=validate.Length(min=3, max=100))
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6, max=100)) # we do not return the password in api response

user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_partial_schema = UserSchema(partial=True)