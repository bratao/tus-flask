=========
tus-flask
=========

A flask filter for the TUS resumable upload protocol for tus protocol 1.0.0, `the tus resumable upload standard`_.

.. _the tus resumable upload standard: http://tus.io/

This code is 100% based upon https://github.com/everydo/tusfilter work. It was modified to work with recent Flask
versions and to keep compatibility with the latest tus protocol

Arguments
---------

app
    required, the wsgi server application

upload_path
    ``str``, required, path of the upload service

tmp_dir
    ``str``, optional, directory to store temporary files, default ``/upload``

expire
    ``int``, optional, how long before cleanup old uploads in seconds, default ``60*60*60``

send_file
    ``bool``, optional, ``False`` for send the absolute filepath in ``tmp_dir`` in the request body,
    ``True`` for an actual file uploaded, default ``False``

max_size
    ``int``, optional, maximum size of uploads in bytes, default ``2**30``, 1G

callback
    A function that is called when the upload was successful

Example
-------

flask ::

    from tusfilter import TusFilter
    from flask import Flask

    app = Flask(__name__)

    def upload_resumable_callback(tmpfile):
        # do something else
        return 'End of upload'

    app.wsgi_app = TusFilter(
        app.wsgi_app,
        upload_path='/upload_resumable',
        tmp_dir='tmp',
        callback=upload_resumable
    )
