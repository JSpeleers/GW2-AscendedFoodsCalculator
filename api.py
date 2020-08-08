import json
import logging

import requests


class Commerce:
    """
    Commerce API
    """
    MAX_API_IDS = 200

    def __init__(self):
        self.ids = []

    def get_prices(self) -> []:
        """
        For each item_id in ids, retrieve the current order and instant buy prices
        :return: list of dicts representing the JSON response of the API
        """
        all_prices = []
        # Call the API for each 200 IDs, then merge responses
        for i in range(0, int(len(self.ids) / self.MAX_API_IDS) + 1):
            request_url = 'https://api.guildwars2.com/v2/commerce/prices?ids={}'.format(
                str(self.ids[i * self.MAX_API_IDS: (i + 1) * self.MAX_API_IDS])[1:-1].replace(" ", "").replace("'", ""))
            logging.debug(request_url)
            request_response = requests.get(request_url)
            logging.debug(request_response)
            all_prices.extend(json.loads(request_response.content))
        return all_prices
