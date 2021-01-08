import os
from dotenv import load_dotenv

load_dotenv()


DEBUG = os.getenv("DEBUG")
REDIRECT_URI = os.getenv("REDIRECT_URI")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")
