from ..model.propertysewer import SewerType, PropertySewer

sewer_type_mapping = {
    SewerType.NONE: "None",
    SewerType.YES: "Yes",
    SewerType.SEPTIC: "Septic",
    SewerType.STORM: "Storm",
    SewerType.MUNICIPAL: "Municipal",
}


def map_propertysewer_to_rest_response(propertySewer: PropertySewer) -> dict:
    """
    Maps model to the response type defined in the Namespace model (SewerResponse)
    """
    return {
        "address": propertySewer.address,
        "zipcode": propertySewer.zip_code,
        "sewertype": sewer_type_mapping[propertySewer.sewer],
    }
