import requests
from typing import Optional
from ..model.propertysewer import SewerType, PropertySewer
from . import mapper


class HomeCanaryApi:
    def __init__(self, config):
        self.base_url = config["HOMECANARY_BASE_URL"]
        self.bearer_token = config["HOMECANARY_API_TOKEN"]

    def _init_auth(self, session):
        session.headers.update({"Authorization": f"Bearer {self.bearer_token}"})

    def get_propertysewer(self, address: str, zip_code: str) -> Optional[PropertySewer]:
        query = {"address": address, "zipcode": zip_code}
        with requests.Session() as session:
            self._init_auth(session)
            response = session.get(f"{self.base_url}/property/details", params=query)
            if response.status_code == 404:
                return None
            elif response.status_code != 200:
                raise Exception(
                    f"Error with HomeCanary API: {response.status_code}: {response.reason}"
                )

            return mapper.map_homecanary_response_to_model(response.json(), query)
