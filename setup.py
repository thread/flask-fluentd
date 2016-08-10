"""
Flask-Fluentd
-------------

This library lets you log fluentd events simply from a Flask application
"""
from setuptools import setup


setup(
    name='Flask-fluentd',
    version='0.2',
    url='https://github.com/thread/flask-fluentd/archive/0.2.tar.gz',
    license='MIT',
    author='Thread',
    author_email='j+flask_fluentd@thread.com',
    description='Log fluentd events from Flask',
    long_description=__doc__,
    py_modules=['flask_fluentd'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'fluent-logger',
        'six',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
