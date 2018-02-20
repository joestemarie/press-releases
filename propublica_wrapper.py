"""Functions to wrap the ProPublica API."""
import json
import pystache
import requests
from keys import PROPUBLICA_API_KEY

def fetch_releases(endpoint, propublica_api_key, **kwargs):
    """Fetch releases from the ProPublic API.

    Args:
        endpoint: an endpoint for the API using moustache tags for params
        propublica_api_key: a valid API key for the Propublica API
        kwargs: all of the params needed to build the endpoint

    Returns:
        A dictionary with the decoded JSON from the ProPublica API.
    """

    # build the full endpoint using the kwargs
    url = "https://api.propublica.org/" + pystache.render(endpoint, kwargs)
    headers = {"X-API-Key": propublica_api_key}
    print("Requesting from:")
    print(url)
    r = requests.get(url, headers=headers)
    parsed_response = json.loads(r.text)
    return parsed_response["results"]

def fetch_releases_by_date(date, propublica_api_key):
    """Get press releases for a specific date.

    Documented by ProPublica here:
    https://projects.propublica.org/api-docs/congress-api/other/#get-congressional-statements-by-date

    Args:
        date: the date that we should get releases for (YYYY-MM-DD format)
        propublica_api_key: a valid API key for ProPublica

    Returns:
        Press releases in a dict object.
    """
    endpoint = "congress/v1/statements/date/{{date}}.json"
    releases = fetch_releases(endpoint, propublica_api_key, date=date)
    return(releases)
