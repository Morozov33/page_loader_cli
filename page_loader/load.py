import os
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from page_loader.names import get_name


def download(download_url, path='cwd'):
    if path == 'cwd':
        path = os.getcwd()
    dir_name = get_name(download_url, is_dir=True)
    dir_path = os.path.join(path, dir_name)
    os.mkdir(dir_path)
    os.chdir(dir_path)
    page_name = get_name(download_url)
    page_load = requests.get(download_url).text
    page_netloc = urlparse(download_url).netloc
    soup = BeautifulSoup(page_load, 'html.parser')
    for img_tag in soup.find_all('img'):
        img_link = img_tag.get('src')
        if urlparse(img_link).netloc in (page_netloc, ''):
            img_link = urljoin(download_url, img_link)
            img_name = get_name(img_link)
            img_path = os.path.join(dir_path, img_name)
            with open(img_path, 'wb') as img:
                img.write(requests.get(img_link).content)
            img_tag['src'] = os.path.join(dir_name, img_name)
        else:
            pass
    for link_tag in soup.find_all('link'):
        link_link = link_tag.get('href')
        if urlparse(link_link).netloc in (page_netloc, ''):
            link_link = urljoin(download_url, link_link)
            link_name = get_name(link_link)
            link_path = os.path.join(dir_path, link_name)
            with open(link_path, 'w') as link:
                link.write(requests.get(link_link).text)
            link_tag['href'] = os.path.join(dir_name, link_name)
        else:
            pass
    for js_tag in soup.find_all('script'):
        js_link = js_tag.get('src')
        if urlparse(js_link).netloc in (page_netloc, ''):
            js_link = urljoin(download_url, js_link)
            js_name = get_name(js_link)
            js_path = os.path.join(dir_path, js_name)
            with open(js_path, 'w') as js:
                js.write(requests.get(js_link).text)
            js_tag['src'] = os.path.join(dir_name, js_name)
        else:
            pass
    os.chdir(path)
    with open(page_name, 'w') as page:
        page.write(soup.prettify())
    return os.path.join(path, page_name)
