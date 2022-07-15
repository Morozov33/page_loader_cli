import tempfile
import os
from page_loader.load import download
from bs4 import BeautifulSoup


original_page_name = 'original_page.html'
original_dir_name = 'original_files'
original_file_img_name = 'nodejs.png'
original_file_css_name = 'application.css'
original_file_js_name = 'runtime.js'
original_url = 'https://ru.hexlet.io/courses'
original_img_url = 'https://ru.hexlet.io/assets/professions/nodejs.png'
original_css_url = 'https://ru.hexlet.io/assets/application.css'
original_js_url = 'https://ru.hexlet.io/packs/js/runtime.js'
original_page_path = os.path.join('.', 'tests', 'fixtures', original_page_name)
original_dir_path = os.path.join('.', 'tests', 'fixtures', original_dir_name)
original_img_path = os.path.join(original_dir_path, original_file_img_name)
original_css_path = os.path.join(original_dir_path, original_file_css_name)
original_js_path = os.path.join(original_dir_path, original_file_js_name)

test_page_name = 'ru-hexlet-io-courses.html'
test_dir_name = 'ru-hexlet-io-courses_files'
test_file_img_name = 'ru-hexlet-io-assets-professions-nodejs.png'
test_file_css_name = 'ru-hexlet-io-assets-application.css'
test_file_js_name = 'ru-hexlet-io-packs-js-runtime.js'
test_files_names = sorted([test_file_img_name, test_file_css_name,
                           test_file_js_name, test_page_name])
test_page_path = os.path.join('.', 'tests', 'fixtures', test_page_name)


with open(test_page_path, 'r') as r:
    test_page = r.read()

with open(original_page_path, 'r') as f:
    original_page = f.read()

with open(original_img_path, 'rb') as s:
    original_file_img = s.read()

with open(original_css_path, 'r') as s:
    original_file_css = s.read()

with open(original_js_path, 'r') as s:
    original_file_js = s.read()


def test_load_page(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_img_url, content=original_file_img)
    requests_mock.get(original_css_url, text=original_file_css)
    requests_mock.get(original_js_url, text=original_file_js)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        download(original_url)
        with open(test_page_name, 'r') as f:
            download_page = f.read()
        assert download_page == test_page


def test_load_image(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_img_url, content=original_file_img)
    requests_mock.get(original_css_url, text=original_file_css)
    requests_mock.get(original_js_url, text=original_file_js)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        download(original_url)
        os.chdir(os.path.join(tmpdir, test_dir_name))
        with open(test_file_img_name, 'rb') as f:
            download_image = f.read()
        assert download_image == original_file_img


def test_load_css(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_img_url, content=original_file_img)
    requests_mock.get(original_css_url, text=original_file_css)
    requests_mock.get(original_js_url, text=original_file_js)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        download(original_url)
        os.chdir(os.path.join(tmpdir, test_dir_name))
        with open(test_file_css_name, 'r') as f:
            download_css = f.read()
        assert download_css == original_file_css


def test_load_js(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_img_url, content=original_file_img)
    requests_mock.get(original_css_url, text=original_file_css)
    requests_mock.get(original_js_url, text=original_file_js)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        download(original_url)
        os.chdir(os.path.join(tmpdir, test_dir_name))
        with open(test_file_js_name, 'r') as f:
            download_js = f.read()
        assert download_js == original_file_js


def test_files_name(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_img_url, content=original_file_img)
    requests_mock.get(original_css_url, text=original_file_css)
    requests_mock.get(original_js_url, text=original_file_js)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        download(original_url)
        os.chdir(test_dir_name)
        with os.scandir() as it:
            list_files_names = []
            for file in it:
                list_files_names.append(file.name)
        assert sorted(list_files_names) == test_files_names


def test_load_html(requests_mock):
    requests_mock.get(original_url, text=original_page)
    requests_mock.get(original_img_url, content=original_file_img)
    requests_mock.get(original_css_url, text=original_file_css)
    requests_mock.get(original_js_url, text=original_file_js)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        download(original_url)
        os.chdir(os.path.join(tmpdir, test_dir_name))
        with open(test_page_name, 'r') as f:
            download_html = f.read()
        assert download_html == original_page
