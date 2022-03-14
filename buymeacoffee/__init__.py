"""Fetch and persist paginated donations to local JSON."""
import json

import requests
from config import (
    BUYMEACOFFEE_API_TOKEN,
    BUYMEACOFFEE_NUM_PAGINATED_RESULTS,
    BUYMEACOFFEE_RESULTS_EXPORT,
    BUYMEACOFFEE_SUPPORTERS_ENDPOINT,
)
from logger import LOGGER
from requests.exceptions import HTTPError


def init_script():
    """Fetch all `BuyMeACoffee` donations and save to local JSON."""
    with open(BUYMEACOFFEE_RESULTS_EXPORT, mode="w") as file:
        file.write("[")
        for i in range(1, BUYMEACOFFEE_NUM_PAGINATED_RESULTS):
            file.write(fetch_page_of_results(i))
        file.write("]")
    LOGGER.success(
        f"Successfully fetched and persisted {BUYMEACOFFEE_NUM_PAGINATED_RESULTS * 5} donations to {BUYMEACOFFEE_RESULTS_EXPORT}"
    )


def fetch_page_of_results(page_num: int) -> str:
    """
    Get single page of donation results.

    :param int page_num: Number of paginated responses.

    :returns: str
    """
    try:
        headers = {
            "content-type": "application/json",
            "connection": "keep-alive",
            "accept": "*/*",
            "Authorization": f"Bearer {BUYMEACOFFEE_API_TOKEN}",
        }
        params = {"page": page_num}
        resp = requests.get(
            BUYMEACOFFEE_SUPPORTERS_ENDPOINT, headers=headers, params=params
        )
        return json.dumps(resp.json()["data"]).replace("[", "").replace("]", "")
    except HTTPError as e:
        LOGGER.error(
            f"HTTPError while fetching page={page_num} of results: {e}"
        )
    except Exception as e:
        LOGGER.error(
            f"Unexpected error while fetching page={page_num} of results: {e}"
        )
