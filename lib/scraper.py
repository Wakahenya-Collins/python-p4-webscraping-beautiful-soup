from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')
url = "https://flatironschool.com/"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    doc = BeautifulSoup(response.text, 'html.parser')

    # Check if there are elements with the class 'heading-financier'
    heading_elements = doc.select('.heading-financier')

    if heading_elements:
        # Access the first element's contents if it exists
        print(doc.select('.heading-financier')[0].contents)
    else:
        print("No elements with class 'heading-financier' found on the page.")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")