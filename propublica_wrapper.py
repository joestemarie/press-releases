"""Functions to wrap the ProPublica API."""
import json
import pystache
import requests
from keys import PROPUBLICA_API_KEY

def fetch_releases(endpoint, propublica_api_key, **kwargs):
    """Fetch releases from the ProPublic API.

    Args:
        endpoint:   an endpoint for the API using moustache tags for params
        kwargs:     all of the params for the endpoint
    """
    url = "https://api.propublica.org/" + pystache.render(endpoint, kwargs)
    headers = {"X-API-Key": propublica_api_key}
    print("Requesting from:")
    print(url)
    r = requests.get(url, headers=headers)
    parsed_response = json.loads(r.text)
    return parsed_response["results"]
