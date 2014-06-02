#!/usr/bin/env python

import flask
from flask_cors import cross_origin 

import StringIO
import dither

import logging
logging.basicConfig(level=logging.DEBUG)

app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():
    rsp = {'stat': 'ok'}
    return flask.jsonify(**rsp)

@app.route('/atk', methods=['GET'])
@cross_origin(methods=['GET'])
def atk():

    # root = app.config.from_envvar('PLUMBING_ATKINSON_SERVER_IMAGE_ROOT')

    d = dither.dither()

    src = flask.request.args.get('path')
    dest = StringIO.StringIO()

    d.dither_image(src, dest, 'GIF')
    dest.seek(0)

    return flask.send_file(dest, mimetype='image/gif')

if __name__ == '__main__':
    debug = True	# sudo make me a CLI option
    app.run(debug=debug)
