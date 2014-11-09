#!/usr/bin/env python

import flask
from flask_cors import cross_origin 

import StringIO
import logging
import os

try:
    # https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-atkinson
    import cooperhewitt.roboteyes.atkinson as atkinson
except Exception, e:
    import atkinson

try:
    # https://github.com/cooperhewitt/py-cooperhewitt-flask
    import cooperhewitt.flask.http_pony as http_pony
except Exception, e:
    import http_pony

app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():

    return flask.jsonify({'stat': 'ok'})

@app.route('/dither', methods=['GET', 'POST'])
def dither():

    try:
        if flask.request.method=='POST':
            path = http_pony.get_upload_path(app)
        else:
            path = http_pony.get_local_path(app)

    except Exception, e:
        logging.error(e)
        flask.abort(400)

    logging.debug("%s %s %s" % (flask.request.method, 'dither', path))

    src = path
    dest = StringIO.StringIO()

    ok = True

    try:
        atkinson.dither(src, dest)
    except Exception, e:
        logging.error("failed to process %s, because %s" % (path, e))
        ok = False

    if flask.request.method=='POST':
        logging.debug("unlink %s" % path)
        os.unlink(path)

    if not ok:
        flask.abort(500)

    dest.seek(0)
    return flask.send_file(dest, mimetype='image/gif')

if __name__ == '__main__':

    import sys
    import optparse
    import ConfigParser

    parser = optparse.OptionParser()

    parser.add_option("-c", "--config", dest="config", help="", action="store", default=None)
    parser.add_option("-v", "--verbose", dest="verbose", help="enable chatty logging; default is false", action="store_true", default=False)

    opts, args = parser.parse_args()

    if opts.verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("verbose logging is enabled")
    else:
        logging.basicConfig(level=logging.INFO)

    cfg = ConfigParser.ConfigParser()
    cfg.read(opts.config)

    http_pony.update_app_config(app, cfg)

    port = cfg.get('flask', 'port')
    port = int(port)

    app.run(port=port)
