# plumbing-atkinson-server

plumbing-atkinson-server is a simple Flask-based HTTP-pony to dither images.

## Install

	python ./setup.py install

## Example

The `setup.py` script will install the atkison-server.py in `/usr/local/bin` (or your operating system's equivalent) but you can also run it directly like this:

	python ./scripts/atkinson-server.py -c server.cfg
	INFO:werkzeug: * Running on http://127.0.0.1:5000/

Or:

	setenv ATKINSON_SERVER_CONFIG server.cfg
	python ./scripts/atkinson-server.py
	INFO:werkzeug: * Running on http://127.0.0.1:5000/

You can also run `atkinson-server` from any WSGI-compliant container-server-thing-y. Consult the [init.d folder](init.d) for an example of how to use `atkinson-server` with [gunicorn](http://gunicorn.org).

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

## See also:

* http://flask.pocoo.org/
* https://pypi.python.org/pypi/Flask-Cors/
* https://github.com/cooperhewitt/py-cooperhewitt-flask
* https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-atkinson
* https://github.com/migurski/atkinson
* http://mike.teczno.com/notes/atkinson.html
* http://en.wikipedia.org/wiki/Bill_Atkinson
