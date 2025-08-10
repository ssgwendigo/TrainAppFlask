import requests
import logging
from flask import current_app


class WMATAHelper:
    BASE_URL = "https://api.wmata.com"

    def __init__(self):
        self.primary_key = current_app.config['WMATA_PRIMARY_API_KEY']
        self.secondary_key = current_app.config['WMATA_SECONDARY_API_KEY']
        self.logger = logging.getLogger(__name__)

    def validate_api_key(self):
        endpoint = "Misc/Validate"
        response = self.make_request(endpoint)
        return bool(response)

    def make_request(self, endpoint, method='GET'):
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {'api_key': self.primary_key}

        try:
            response = requests.request(method, url, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            self.logger.error(f"API request failed: {str(e)}")
            return None