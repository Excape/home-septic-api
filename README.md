# Home Septic API

> A small API wrapper to read sewer information for a property from the HomeCanary API

## Setup

Prerequisites: `Python 3.9` and `pip` are installed

### Run locally

1. Clone this repo
1. Install the package with `pip3 install .`
1. Adjust the settings in `config.py` if needed
1. Run `flask run` to start the server

### Setup for Development

- Run `pip3 install -r requirements.txt`
- Run the app with `python app.py`
- Run tests with `pytest`

## Usage

- Once the server has started, the Swagger API is available on <http://localhost:5000/api/doc>, the API itself runs on <http://localhost:5000/api/sewer>

- The HomeCanary API is not publicly available. I've created a mock with the same API structure that can be tested with Swagger here: <https://app.swaggerhub.com/apis-docs/robinsuter/HouseCanary/v2>. This app uses the mock by default (configurable with `config.py`)

- The API uses a fake authorization with an API key for demo purposes. For a request to succeed, a header `X-API-KEY` with any value needs to be set.

## Libraries

- `Flask` as a minimal web framework
- `flask-restplus` to provide an OpenAPI specification and a Swagger UI
- `requests` as an HTTP library to request the HomeCanary API
- `pytest` for testing
