import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()


setup(
    name='tus-flask',
    version='0.1.0',
    description='A flask filter for the TUS resumable upload protocol',
    long_description=long_description,
    url='bratao/tus-flask',
    author='bratao',
    author_email='bruno@potelo.com.br',
    keywords='tus flask filter',
    license='MIT',

    py_modules=['tusfilter'],
    install_requires=['WebOb'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'License :: OSI Approved :: MIT License',
    ],
)
