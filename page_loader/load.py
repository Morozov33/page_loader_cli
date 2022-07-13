import os
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


def get_name(url, type_):
    parse_url = urlparse(url)
    name = f"{parse_url.netloc}{parse_url.path}".replace('.', '-')
    name = name.replace('/', '-')
    if type_ == 'page':
        name = f"{name}.html"
    elif type_ == 'image':
        if name[-3::] == 'png':
            name = f"{name[:-4:]}.png"
        elif name[-3::] == 'jpg':
            name = f"{name[:-4:]}.jpg"
    elif type_ == 'dir':
        name = f"{name}_files"
    return name


def download(download_url, path='cwd'):
    dir_not_created = True
    if path == 'cwd':
        path = os.getcwd()
    os.chdir(path)
    page_name = get_name(download_url, 'page')
    page_load = requests.get(download_url).text
    soup = BeautifulSoup(page_load, 'html.parser')
    for image_tag in soup.find_all('img', src=True):
        image_link = image_tag.get('src')
        image_path = urljoin(download_url, image_link)
        if dir_not_created:
            dir_name = get_name(download_url, 'dir')
            dir_path = os.path.join(path, dir_name)
            os.mkdir(dir_path)
            dir_not_created = False
        image_name = get_name(image_path, 'image')
        full_path_to_file = os.path.join(dir_path, image_name)
        with open(full_path_to_file, 'wb') as img:
            img.write(requests.get(image_path).content)
        image_tag['src'] = os.path.join(dir_name, image_name)
    with open(page_name, 'w') as page:
        page.write(soup.prettify())
    return os.path.join(path, page_name)
