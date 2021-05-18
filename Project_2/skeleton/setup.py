try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project_2',
    'author': 'Vincent Zhou',
    'url': 'www.abc.com',
    'download_url': 'www.abc.com/download',
    'author_email': 'zy7ljv@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Project_2'
}

setup(**config)