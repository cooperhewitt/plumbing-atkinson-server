#!/usr/bin/env python

import flask
from flask_cors import cross_origin 

import StringIO
import logging

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

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():

    return flask.jsonify({'stat': 'ok'})

@app.route('/dither', methods=['GET'])
def dither():

    dest = StringIO.StringIO()

    try:
        atkinson.dither()
    except Exception, e:
        logging.error("failed to dither")
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

    app.run()
