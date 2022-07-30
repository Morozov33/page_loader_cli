import os
import requests
import logging
from page_loader.names import get_name
from urllib.parse import urlparse, urljoin
from progress.bar import Bar
from concurrent import futures


def get_file(soup, url_, type_):
    if type_ == 'link':
        type_link = 'href'
    elif type_ in ('img', 'script'):
        type_link = 'src'
    type_file = 'wb' if type_ == 'img' else 'w'
    page_netloc = urlparse(url_).netloc
    tags = [x for x in soup.find_all(type_)
            if urlparse(x.get(type_link)).netloc in (page_netloc, '')]
    bar = Bar(f"Downloading {type_} files:",
              max=len(tags),
              suffix='%(index)d/%(max)d')
    with futures.ThreadPoolExecutor(max_workers=8) as executor, bar:
        tasks = [executor.submit(load_save_file, tag, url_, type_,
                                 type_link, type_file, page_netloc, bar
                                 ) for tag in soup.find_all(type_)]
        bar.finish()
        result = [task.result() for task in tasks]
        logging.info(f"All assets was downloaded: {result}")


def load_save_file(tag, url_, type_, type_link, type_file, page_netloc, bar):
    if urlparse(tag.get(type_link)).netloc in (page_netloc, ''):
        link = urljoin(url_, tag.get(type_link))
        name = get_name(link)
        path = os.path.join(os.getcwd(), name)
        with open(path, type_file) as file:
            try:
                download_file = requests.get(link)
                download_file.raise_for_status()
                bar.next()
            except IOError as request_err:
                logging.error(f"{request_err}")
                raise
            else:
                if type_ == 'img':
                    file.write(download_file.content)
                elif type_ in ('link', 'script'):
                    file.write(download_file.text)
        tag[type_link] = os.path.join(os.path.basename(os.getcwd()), name)
