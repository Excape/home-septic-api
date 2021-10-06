import requests
from typing import Optional
from .model.propertysewer import SewerType, PropertySewer

class HomeCanaryApi:
    def __init__(self, config):
        self.base_url = config["HOMECANARY_BASE_URL"]
        self.bearer_token = config["HOMECANARY_API_TOKEN"]

    def _initAuth(self, session):
        session.headers.update({"Authorization": f"Bearer {self.bearer_token}"})

    def getPropertyDetails(self, address: str, zip_code: str) -> Optional[PropertySewer]:
        query = {"address": address, "zipcode": zip_code}
        with requests.Session() as session:
            self._initAuth(session)
            response = session.get(f"{self.base_url}/property/details", params=query)
            if response.status_code == 404:
                return None
            elif response.status_code != 200:
                raise Exception(f"Error with HomeCanary API: {response.status_code}: {response.reason}")
               

            return self._mapToModel(response.json(), query)

    def _mapToModel(self, response, query):
        property = response["result"]["property"]
        sewerType = self._mapSewerType(property["sewer"])
        return PropertySewer(query["address"], query["zipcode"], sewerType)


    def _mapSewerType(self, sewerType: str) -> SewerType:
        mappings = {
            "None": SewerType.NONE,
            "Municipal": SewerType.MUNICIPAL,
            "Storm": SewerType.STORM,
            "Septic": SewerType.SEPTIC,
            "Yes": SewerType.YES
        }
        try:
            return mappings[sewerType]
        except KeyError:
            raise Exception(f"Sewer in response is invalid: {sewerType}")
        
          