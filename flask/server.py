#!/usr/bin/env python

import flask
from flask_cors import cross_origin 
from werkzeug.security import safe_join

import StringIO
import dither

import os
import os.path
import logging
logging.basicConfig(level=logging.INFO)

app = flask.Flask(__name__)
app.config['USE_X_SENDFILE'] = True

# Quick. And dirty. To figure out:
# http://flask.pocoo.org/docs/config/
# https://github.com/mbr/flask-appconfig
# (20140602/straup)

if os.environ.get('ATKINSON_SERVER_IMAGE_ROOT', None):
    app.config['ATKINSON_SERVER_IMAGE_ROOT'] = os.environ['ATKINSON_SERVER_IMAGE_ROOT']

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():
    rsp = {'stat': 'ok'}
    return flask.jsonify(**rsp)

@app.route('/atk', methods=['GET'])
def atk():

    src = flask.request.args.get('path')
    logging.debug("request path is %s" % src)

    root = app.config.get('ATKINSON_SERVER_IMAGE_ROOT', None)

    if root:
        safe = safe_join(root, src)

        if not safe:
            logging.error("'%s' + '%s' considered harmful" % (root, src))
            flask.abort(400)

        src = safe

    logging.debug("final request path is %s" % src)
    
    if not os.path.exists(src):
        logging.error("%s does not exist" % src)
        flask.abort(404)

    dest = StringIO.StringIO()

    d = dither.dither()
    d.dither_image(src, dest, 'GIF')

    dest.seek(0)
    return flask.send_file(dest, mimetype='image/gif')

if __name__ == '__main__':
    debug = True	# sudo make me a CLI option
    app.run(debug=debug)
