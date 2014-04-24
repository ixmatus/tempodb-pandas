
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.org", "r") as f:
    README = f.read()

config = {
    'description': README,
    'author': 'Parnell Springmeyer',
    'url': 'https://github.com/ixmatus/tempodb-pandas',
    'download_url': 'https://github.com/ixmatus/tempodb-pandas',
    'author_email': 'parnell@ixmat.us',
    'version': '0.1',
    'install_requires': [
        'nose',
        'pandas'
    ],
    'packages': ['tempodb-pandas'],
    'scripts': [],
    'name': 'tempodb-pandas'
}

setup(**config)
