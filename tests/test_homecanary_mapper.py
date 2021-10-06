import pytest

from home_septic_api.model.propertysewer import SewerType, PropertySewer
from home_septic_api.homecanary import mapper

def homecanary_response(sewer_type: str):
    return {
        "result": {
            "property": {
                "sewer": sewer_type
            }
    }
}

query = {"address": "3 Beale St", "zipcode": "02000"}

params = [
    (homecanary_response('None'), SewerType.NONE),
    (homecanary_response('Septic'), SewerType.SEPTIC),
    (homecanary_response('Storm'), SewerType.STORM),
    (homecanary_response('Municipal'), SewerType.MUNICIPAL),
    (homecanary_response('Yes'), SewerType.YES),
]
@pytest.mark.parametrize("response, expected_sewer_type", params)
def test_map_possible_sewer_types(response, expected_sewer_type):
    actual = mapper.map_homecanary_response_to_model(response, query)
    expected = PropertySewer(query["address"], query["zipcode"], expected_sewer_type)

    assert actual == expected

def test_map_invalid_sewer_type():
    response = homecanary_response('INVALID_TYPE')
    with pytest.raises(Exception):
        mapper.map_homecanary_response_to_model(response, query)