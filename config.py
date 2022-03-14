from os import getenv, path

from dotenv import load_dotenv

# Load variables from .env
BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

# Logging config
ENVIRONMENT = getenv("ENVIRONMENT")
PROJECT_NAME = "buymeacoffee-fetcher"
PROJECT_LOG_DIRECTORY = f"/var/log/{PROJECT_NAME}"

# API Config
BUYMEACOFFEE_API_TOKEN = getenv("BUYMEACOFFEE_API_TOKEN")
BUYMEACOFFEE_SUPPORTERS_ENDPOINT = (
    "https://developers.buymeacoffee.com/api/v1/supporters"
)
BUYMEACOFFEE_NUM_PAGINATED_RESULTS = 19  # TODO: Make value dynamic
BUYMEACOFFEE_RESULTS_EXPORT = f"{BASE_DIR}/export/donations.json"
