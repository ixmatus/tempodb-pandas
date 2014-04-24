
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
        'numpy >= 1.8.1',
        'pandas >= 0.13.1',
        'tempodb >= 0.5.0',
        'six'
    ],
    'packages': ['tempodb_pandas'],
    'scripts': [],
    'name': 'tempodb-pandas'
}

setup(**config)
