import requests
import json
from config import BUYMEACOFFEE_SUPPORTERS_ENDPOINT, BUYMEACOFFEE_API_TOKEN


def init_script():
    """Fetch all `BuyMeACoffee` donations and save to local JSON."""
    with open("donations.json", mode="w") as file:
        file.write("[")
        for i in range(1, 19):
            file.write(fetch_page_of_results(i))
        file.write("]")


def fetch_page_of_results(page_num: int) -> str:
    """
    Get single page of donation results.

    :param int page_num: Number of paginated responses.

    :returns: str
    """
    headers = {
        "content-type": "application/json",
        "connection": "keep-alive",
        "accept": "*/*",
        "Authorization": f"Bearer {BUYMEACOFFEE_API_TOKEN}"
    }
    params = {"page": page_num}
    resp = requests.get(BUYMEACOFFEE_SUPPORTERS_ENDPOINT, headers=headers, params=params)
    return json.dumps(resp.json()["data"]).replace("[", "").replace("]", "")
