import requests, json, http.client
from bs4 import BeautifulSoup

url = str(input("Masukkan subdomain: "))
reqs = requests.get("http://" + url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    print(link.get('href'))