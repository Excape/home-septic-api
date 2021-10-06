import pytest
from home_septic_api.model.propertysewer import SewerType, PropertySewer
from home_septic_api.rest import mapper

address = "10 3rd Ave"
zip_code = "01007"


def property_sewer(sewer_type: SewerType):
    return PropertySewer(address, zip_code, sewer_type)

params = [
    (property_sewer(SewerType.NONE), 'None'),
    (property_sewer(SewerType.SEPTIC), 'Septic'),
    (property_sewer(SewerType.STORM), 'Storm'),
    (property_sewer(SewerType.MUNICIPAL), 'Municipal'),
    (property_sewer(SewerType.YES), 'Yes'),
]

@pytest.mark.parametrize("property_sewer, expected_sewer_type", params)
def test_map_propertysewer_to_rest_response(property_sewer, expected_sewer_type):
    actual = mapper.map_propertysewer_to_rest_response(property_sewer)
    expected = {
        "address": address,
        "zipcode": zip_code,
        "sewertype": expected_sewer_type
    }
    
    assert actual == expected