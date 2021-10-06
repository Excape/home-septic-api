from ..model.propertysewer import PropertySewer, SewerType

def map_homecanary_response_to_model(response, query):
        property = response["result"]["property"]
        sewerType = _map_sewer_type(property["sewer"])
        return PropertySewer(query["address"], query["zipcode"], sewerType)

def _map_sewer_type(sewerType: str) -> SewerType:
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
