from urllib.parse import urlparse


def get_name(url_, is_dir=False):
    url = urlparse(url_)
    name = f"{url.netloc}{url.path}".replace('.', '-').replace('/', '-')
    if is_dir:
        name = f"{name}_files"
    else:
        if name[-4::] == '-png':
            name = f"{name[:-4:]}.png"
        elif name[-4::] == '-jpg':
            name = f"{name[:-4:]}.jpg"
        elif name[-4::] == '-css':
            name = f"{name[:-4:]}.css"
        elif name[-3::] == '-js':
            name = f"{name[:-3:]}.js"
        else:
            name = f"{name}.html"
    return name
