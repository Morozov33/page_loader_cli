import os
import requests
from urllib.parse import urlparse


def get_name_file(url):
    parse_url = urlparse(url)
    name_file = f"{parse_url.netloc}{parse_url.path}".replace('.', '-')
    name_file = name_file.replace('/', '-')
    name_file = f"{name_file}.html"
    return name_file


def download(download_url, path_to_file='cwd'):
    if path_to_file == 'cwd':
        path_to_file = os.getcwd()
    os.chdir(path_to_file)
    file_name = get_name_file(download_url)
    with open(file_name, 'w') as file:
        file.write(requests.get(download_url).text)
    return os.path.join(path_to_file, file_name)
