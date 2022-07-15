from urllib.parse import urlparse


def get_name(url_, is_dir=False):
    url = urlparse(url_)
    name = f"{url.netloc}{url.path}".replace('.', '-').replace('/', '-')
    name = name[:-1:] if name.endswith('-') else name
    if is_dir:
        name = f"{name}_files"
    else:
        if name.endswith('-png'):
            name = f"{name[:-4:]}.png"
        elif name.endswith('-jpg'):
            name = f"{name[:-4:]}.jpg"
        elif name.endswith('-css'):
            name = f"{name[:-4:]}.css"
        elif name.endswith('-js'):
            name = f"{name[:-3:]}.js"
        else:
            name = f"{name}.html"
    return name
