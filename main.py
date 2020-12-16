import requests
import requests.sessions
from bs4 import BeautifulSoup
import sqlite3

send_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.5"}


def get_max_page_index():
    r = requests.get(
        "https://git.centos.org/?sorting=None&page=1", headers=send_headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    pagination = soup.select("li.page-item:nth-child(2) > a:nth-child(1)")
    index = pagination[0].string.split(' ')[-1]
    return index


if __name__ == "__main__":
    #max_page_index = get_max_page_index()
    r = requests.get(
        "https://git.centos.org/?sorting=None&page=1", headers=send_headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    pagination = soup.select(
        "#home > div.bodycontent > div.container.mt-5 > div:nth-child(2)")
    print(type(pagination))
