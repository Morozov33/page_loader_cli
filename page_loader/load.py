import os
import requests
import logging
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from page_loader.names import get_name
from page_loader.files import get_file


def download(download_url, path='cwd'):
    if path == 'cwd':
        path = os.getcwd()
    try:
        dir_name = get_name(download_url, is_dir=True)
        dir_path = os.path.join(path, dir_name)
        os.mkdir(dir_path)
        os.chdir(dir_path)
    except FileExistsError:
        logging.error(f"Directory {dir_name} already exists")
        raise
    except FileNotFoundError:
        logging.error(f"Path {path} not found.")
        raise
    except PermissionError:
        logging.error(f"No access rights to directory {dir_name}")
        raise
    except NotADirectoryError:
        logging.error(f"{dir_name} is not directory")
        raise
    else:
        logging.info(f"Directory {dir_name} for files is created")
    try:
        page_name = get_name(download_url)
        page_load = requests.get(download_url)
        page_load.raise_for_status()
    except IOError as request_err:
        logging.error(f"{request_err} to path {download_url}")
        raise
    else:
        logging.info(f"Original page {download_url} is download")
        soup = BeautifulSoup(page_load.text, 'html.parser')
    try:
        get_file(soup, download_url, type_='img')
        get_file(soup, download_url, type_='link')
        get_file(soup, download_url, type_='script')
    except IOError:
        raise
    else:
        os.chdir(path)
        with open(page_name, 'w') as page:
            page.write(soup.prettify())
            logging.info(f"HTML-file {page_name} is created to path: {path}")
