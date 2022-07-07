import tempfile
import os
import requests_mock
from page_loader import download


test_file_name = 'ru-hexlet-io-courses.html'
test_page_path = os.path.join('.', 'tests', 'fixtures', test_file_name)
download_url = 'https://ru.hexlet.io/courses'

@requests_mock.Mocker()
def test_load_page(mock):
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(test_page_path, 'r') as r:
            result_page = r.read()
            mock.get(download_url, text=result_page)
            download(tmpdir)
            with os.scandir(tmpdir) as it:
                for file in it:
                    if file.is_file():
                        with open(file, 'r') as f:
                            download_page = f.read()
                            assert download_page == result_page
                    else:
                        raise Exception('Download file not found!')


@requests_mock.Mocker()
def test_name_load_page(mock):
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(test_page_path, 'r') as r:
            result_page = r.read()
            mock.get(download_url, text=result_page)
            download(tmpdir)
            with os.scandir(tmpdir) as it:
                for file in it:
                    if file.is_file():
                        assert file.name == test_page_name
                    else:
                        raise Exception('Download file not found!')


@requests_mock.Mocker()
def test_path_load_page(mock):
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(test_page_path, 'r') as r:
            result_page = r.read()
            mock.get(download_url, text=result_page)
            download(tmpdir)
            with os.scandir(tmpdir) as it:
                for file in it:
                    if file.is_file():
                        assert file.path == test_page_path
                    else:
                        raise Exception('Download file not found!')
