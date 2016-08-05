"""
Flask-Fluentd
-------------

This library lets you log fluentd events simply from a Flask application
"""
from setuptools import setup


setup(
    name='Flask-fluentd',
    version='0.1',
    url='http://github.com/thread/flask-fluentd/',
    license='Proprietary',
    author='Thread',
    author_email='j+flask_fluentd@thread.com',
    description='Log fluentd events from Flask',
    long_description=__doc__,
    py_modules=['flask_fluentd'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
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
