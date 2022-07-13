import tempfile
import os
from urllib.parse import urljoin
from page_loader.load import download


original_page_name = 'original_page.html'
original_page_path = os.path.join('.', 'tests', 'fixtures', original_page_name)
original_url = 'https://ru.hexlet.io/courses'
original_file_name = 'python.png'
original_file_path = os.path.join('.', 'tests', 'fixtures',
                                  'original_page_files', original_file_name)
original_file_url = 'https://ru.hexlet.io/assets/python.png'
test_page_name = 'ru-hexlet-io-courses.html'
test_file_name = 'ru-hexlet-io-assets-python.png'
test_dir_name = 'ru-hexlet-io-courses_files'
test_page_path = os.path.join('.', 'tests', 'fixtures', test_page_name)
test_file_path = os.path.join('.', 'tests', 'fixtures', test_dir_name,
                              test_file_name)

with open(test_page_path, 'r') as r:
    test_page = r.read()

with open(original_page_path, 'r') as f:
    original_page = f.read()

with open(original_file_path, 'rb') as s:
    original_file = s.read()


def test_load_page(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_file_url, content=original_file)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        download(original_url)
        with os.scandir(tmpdir) as it:
            for file in it:
                if file.is_file():
                    with open(file, 'r') as f:
                        download_page = f.read()
                        assert download_page == test_page


def test_path_load_page(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_file_url, content=original_file)
    count_files = 0
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        with os.scandir(tmpdir) as it:
            for file in it:
                if file.is_file():
                    count_files += 1
        assert count_files == 0
        download(original_url)
        with os.scandir(tmpdir) as it:
            for file in it:
                if file.is_file():
                    count_files += 1
                    assert file.name == test_page_name
        assert count_files == 1


def test_dir_path(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_file_url, content=original_file)
    count_dir = 0
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        with os.scandir(tmpdir) as it:
            for directory in it:
                if directory.is_dir():
                    count_dir += 1
        assert count_dir == 0
        download(original_url)
        with os.scandir(tmpdir) as it:
            for directory in it:
                if directory.is_dir():
                    count_dir += 1
                    assert directory.name == test_dir_name
        assert count_dir == 1


def test_return_path(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_file_url, content=original_file)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        tmp_file_path = os.path.join(os.getcwd(), test_page_name)
        assert download(original_url) == tmp_file_path


def test_files_name(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_file_url, content=original_file)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        download(original_url)
        path_tmp_dir = os.path.join(tmpdir, test_dir_name)
        with os.scandir(path_tmp_dir) as it:
            for file in it:
                assert file.name == test_file_name
