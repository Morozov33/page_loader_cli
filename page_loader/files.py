import os
import requests
import logging
from page_loader.names import get_name
from urllib.parse import urlparse, urljoin


def get_file(soup, url_, type_):
    if type_ == 'link':
        type_link = 'href'
    elif type_ in ('img', 'script'):
        type_link = 'src'
    type_file = 'wb' if type_ == 'img' else 'w'
    page_netloc = urlparse(url_).netloc
    for tag in soup.find_all(type_):
        link = tag.get(type_link)
        if urlparse(link).netloc in (page_netloc, ''):
            link = urljoin(url_, link)
            name = get_name(link)
            path = os.path.join(os.getcwd(), name)
            with open(path, type_file) as file:
                try:
                    download_file = requests.get(link)
                    download_file.raise_for_status()
                except IOError as request_err:
                    logging.error(f"{request_err}")
                    raise
                else:
                    if type_ == 'img':
                        file.write(download_file.content)
                    elif type_ in ('link', 'script'):
                        file.write(download_file.text)
            tag[type_link] = os.path.join(os.path.basename(os.getcwd()), name)
            logging.info(f"File {name} is download")
