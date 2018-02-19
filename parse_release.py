"""Functions to handle requesting and parsing releases."""

# libraries
import requests
from bs4 import BeautifulSoup

def get_release_grafs(url):
    """Parse release paragraphs.

    For a press release URL, download the page and get all of the text within Sanctuary
    <p> tags on the page. Uses requests to download and BeautifulSoup to parse.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    grafs = soup.find_all('p')
    graf_text = [x.text for x in grafs]

    return graf_text
