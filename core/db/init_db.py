from core.db.models import get_user_collection

# makes sure users can't be added if their mail already exists in the db
def initialize_indexes():
    user_collection = get_user_collection()
    user_collection.create_index("email", unique=True)
