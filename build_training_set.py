"""A script to build the training/testing/validation sets for the statement classifier."""

from parse_release import *
from keys import PROPUBLICA_API_KEY

# build a list of every date in 2018 so far to request releases for all of those dates
dates = []
releases = []
for date in dates:
    results = fetch_releases_by_date(date, propublica_api_key=PROPUBLICA_API_KEY)
    releases.extend(results)
