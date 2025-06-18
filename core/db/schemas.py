from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, EXCLUDE, post_dump

ma = Marshmallow()

class UserSchema(ma.Schema):
    
    class Meta:
        unknown = EXCLUDE # makes sure unknown fields in the request aren't added to the db

    id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=3, max=100))
    email = fields.Email(required=True, validate=validate.Length(min=3, max=100))
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6, max=100)) # we do not return the password in api response

    @post_dump(pass_original=True)
    # Converts the mongodb `_id` field to `id` before displaying it for a cleaner API output
    def add_id_field(self, data, original, **kwargs):
        if "_id" in original:
            data["id"] = str(original["_id"])
        return data

user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_partial_schema = UserSchema(partial=True)