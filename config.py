from os import getenv, path
from dotenv import load_dotenv

# Load variables from .env
BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


BUYMEACOFFEE_API_TOKEN = getenv("BUYMEACOFFEE_API_TOKEN")
BUYMEACOFFEE_SUPPORTERS_ENDPOINT = "https://developers.buymeacoffee.com/api/v1/supporters"

