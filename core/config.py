import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "dont-even-think-of-pushing-to-prod-with-this")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/your_db_name")
