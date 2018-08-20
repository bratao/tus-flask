from tusfilter import TusFilter
from flask import Flask

app = Flask(__name__)


def upload_resumable_callback(tmpfile):
    # do something else
    return 'End of upload'


app.wsgi_app = TusFilter(
    app.wsgi_app,
    tmp_dir='/tmp/upload',
    upload_path='/upload_resumable',
    callback=upload_resumable_callback
)
