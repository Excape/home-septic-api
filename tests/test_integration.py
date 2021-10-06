import pytest

from home_septic_api import create_app
from flask.testing import FlaskClient
from flask import json


@pytest.fixture
def app():

    app = create_app(
        {
            "HOMECANARY_BASE_URL": "https://virtserver.swaggerhub.com/robinsuter/HouseCanary/v2",
            "HOMECANARY_API_TOKEN": "12345",
        }
    )

    return app


@pytest.fixture
def client(app) -> FlaskClient:
    return app.test_client()


query = {"address": "205 Worchester St", "zipcode": "02117"}


def test_valid_request(client: FlaskClient):

    response = _send_request(client, query, {"X-API-KEY": "test"})

    result = json.loads(response.data)
    expected = {**query, "sewertype": "Municipal"}

    assert result == expected


def test_unauthorized_request(client: FlaskClient):
    response = _send_request(client, query)
    assert response.status == "401 UNAUTHORIZED"


def test_property_not_found(client: FlaskClient, mocker):
    def mock_get_propertysewer_return_none(self, address, zipcode):
        return None

    _patch_homecanary_api(mocker, mock_get_propertysewer_return_none)

    response = _send_request(client, query, {"X-API-KEY": "test"})

    assert response.status == "404 NOT FOUND"


def test_api_raises_error(client: FlaskClient, mocker):
    def mock_get_propertysewer_raise_error(self, address, zipcode):
        raise Exception("Some error occured")

    _patch_homecanary_api(mocker, mock_get_propertysewer_raise_error)

    response = _send_request(client, query, {"X-API-KEY": "test"})

    assert response.status == "500 INTERNAL SERVER ERROR"


def _patch_homecanary_api(mocker, mockFn):
    mocker.patch(
        "home_septic_api.rest.homesepticresource.HomeCanaryApi.get_propertysewer",
        mockFn,
    )


def _send_request(client, query, headers=None):
    return client.get("/api/sewer", query_string=query, headers=headers)
