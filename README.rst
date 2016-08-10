=============
Flask Fluentd
=============

A library to log fluent events from Flask applications

Installation
============

::

    pip install flask-fluentd

Configuration
=============

Takes just one configuration setting, of ``EVENT_TAG_PREFIX``, which is prepended
to the tag of all outgoing events.

Usage
=====

::

    from flask import Flask, g
    from flask_fluentd import Fluentd


    app = Flask(__name__)
    events = Fluentd(app)

    @app.before_request
    def before_request():
        g.events = events

    # ...

    @app.route('/')
    def index():
        g.events.event(('test', {'foo': 'bar'})

