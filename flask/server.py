#!/usr/bin/env python

import flask
from flask_cors import cross_origin 
from werkzeug.security import safe_join

import StringIO
import dither

import os.path
import logging
logging.basicConfig(level=logging.DEBUG)

app = flask.Flask(__name__)
app.config['USE_X_SENDFILE'] = True

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():
    rsp = {'stat': 'ok'}
    return flask.jsonify(**rsp)

@app.route('/atk', methods=['GET'])
@cross_origin(methods=['GET'])
def atk():

    src = flask.request.args.get('path')
    logging.info("request path is %s" % src)

    root = app.config.get('PLUMBING_ATKINSON_SERVER_IMAGE_ROOT', None)

    if root:
        src = safe_join(root, src)
        logging.info("request path is now '%s'" % src)     

        if not src:
            flask.abort(400)

    if not os.path.exists(src):
        flask.abort(404)

    dest = StringIO.StringIO()

    d = dither.dither()
    d.dither_image(src, dest, 'GIF')

    dest.seek(0)
    return flask.send_file(dest, mimetype='image/gif')

if __name__ == '__main__':
    debug = True	# sudo make me a CLI option

    app.config['PLUMBING_ATKINSON_SERVER_IMAGE_ROOT'] = 'foo'
    app.run(debug=debug)
