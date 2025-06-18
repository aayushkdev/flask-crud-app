from pymongo.errors import DuplicateKeyError
from werkzeug.security import generate_password_hash
from core.db.schemas import user_schema, users_schema
from core.utils import validate_object_id

class UserService:
    def __init__(self, collection):
        self.collection = collection

    def get_by_id(self, id_str):
        object_id = validate_object_id(id_str)
        user = self.collection.find_one({"_id": object_id})
        if not user:
            raise ValueError("User not found")
        return user_schema.dump(user)
    
    def get_all(self):
        users = list(self.collection.find())
        return users_schema.dump(users)

    def create(self, user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        try:
            result = self.collection.insert_one(user_data)
            return str(result.inserted_id)
        except DuplicateKeyError:
            raise ValueError("Email already exists")

    def update(self, id_str, user_data):
        object_id = validate_object_id(id_str)

        if not user_data:
            raise ValueError("No update fields provided")

        if "password" in user_data:
            user_data["password"] = generate_password_hash(user_data["password"])

        try:
            result = self.collection.update_one(
                {"_id": object_id},
                {"$set": user_data}
            )
            if result.matched_count == 0:
                raise ValueError("User not found")
        except DuplicateKeyError:
            raise ValueError("Email already exists")

    def delete(self, id_str):
        object_id = validate_object_id(id_str)
        result = self.collection.delete_one({"_id": object_id})
        if result.deleted_count == 0:
            raise ValueError("User not found")
