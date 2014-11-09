# plumbing-atkinson-server

plumbing-atkinson-server is a simple Flask-based HTTP-pony to dither images.

## Setup

	python ./flask/server.py -c server.cfg
	INFO:werkzeug: * Running on http://127.0.0.1:5000/

## Endpoints

### GET /ping 

	curl -X GET 'http://localhost:5000/ping'

	{
		"stat": "ok"
	}

### GET /dither

	curl -X GET 'http://localhost:5000/dither?file=test.png'

### POST /dither

	curl -X POST -F 'file=@/tmp/test.jpg' 'http://localhost:5000/dither'

## Config

`plumbing-atkinson-server` uses utility functions exported by the
[cooperhewitt.flask.http_pony](https://github.com/cooperhewitt/py-cooperhewitt-flask/blob/master/cooperhewitt/flask/http_pony.py)
library which checks your Flask application's configuration for details about
how to handle things.

The following settings should be added to a standard [ini style configutation
file](https://en.wikipedia.org/wiki/INI_file).

### [flask]

#### port

The Unix TCP port you want your Flask server to listen on.

### [http_pony]

#### local_path_root

If set then files sent using an `HTTP GET` parameter will be limited to only
those that are are parented by this directory.

If it is not set then `HTTP GET` requests will fail.

#### upload_path_root

If set then files sent as an `HTTP POST` request will be first written to this
directory before processing.

If not set then the operating system's temporary directory will be used.

#### allowed_extensions

A comma-separate list of valid file extensions for processing.

## Dependencies

### Things you'll need to install yourself

_Pending a proper `setup.py` file._

* [Flask](http://flask.pocoo.org/)
* [Flask-Cors](https://pypi.python.org/pypi/Flask-Cors/)

### Things that come pre-bundled

_The following are required but are available as libraries local to the server itself if not already pre-installed._

* [cooperhewitt.flask.http_pony](https://github.com/cooperhewitt/py-cooperhewitt-flask)
* [cooperhewitt.roboteyes.atkinson](https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-atkinson)

## To do:

* A proper `setup.py` file

## See also:

* https://github.com/migurski/atkinson
* http://mike.teczno.com/notes/atkinson.html
* http://en.wikipedia.org/wiki/Bill_Atkinson
