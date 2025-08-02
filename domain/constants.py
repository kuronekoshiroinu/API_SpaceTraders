import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("SPACETRADERS_TOKEN")

BASE_URL = "https://api.spacetraders.io/v2"
ACCOUNT_HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
AUTHORIZATION_HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
}