# Console Template

set up basic console environment, and you can quickly develop with it.

## Set Up


### Install pip3

* linux ubuntu

```
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev
```

* mac

```
$ brew install python3
```

### Set up virtual environment

make sure your python verson > 3.4.0

```
$ pyvenv .venv
$ source .venv/bin/activate
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
```

if pyvenv can't work, please use `virtualenv` instead

```
$ pip3 install virtualenv
$ virtualenv .venv
$ source .venv/bin/activate
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
```

## For Fornt-end Developer

### Change type to 'testing' mode

> src/\__init__.py

``` 
...
app.config.from_object(config['testing'])
...

```

### run Flask service

```
$ python3 run.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 249-982-497
```

after run Flask service you can develope at local site

P.S put your code in `src/static` folder.
 

## Folder Explanation

* src: source code

NOTICE: If you add a new python file in src. Please import it in `__init__.py`.
NOTICE: Put yor html, css, JS code in src/static folder.

* docs: api document
* tests: unit tests & api tests
* config.py: configuration of flask, database, donaim name.

NOTICE: make sure your config.py is correct before run the service.

## Flask-cli

* export fisrt

```
$ export FLASK_APP=run.py
or 
$ export path/to/your/run.py
```

* use help command to help you

```
$ flask --help
Usage: flask [OPTIONS] COMMAND [ARGS]...

  This shell command acts as general utility script for Flask applications.

  It loads the application configured (through the FLASK_APP environment
  variable) and then provides commands either provided by the application or
  Flask itself.

  The most useful commands are the "run" and "shell" command.

  Example usage:

    $ export FLASK_APP=hello.py
    $ export FLASK_DEBUG=1
    $ flask run

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  initdb       Initialize the database.
  list_routes  List all routes on flask service
  renewdb      Remove the database.
  run          Runs a development server.
  shell        Runs a shell in the app context.
```

## Documenting

I use apidoc to generate api documents and please check the reference.

### Install

```
$ npm install apidoc -g
```

### Usage

```
$ cd docs
$ apidoc -i ./src -o ./out
```

### Reference

* http://apidocjs.com/

## Testing

### Pre

using pytest, make sure you have installed pytest. 

### Install

```
$ pip3 install pytest
```

### Usage

```
$ pytest # at root folder
=================== test session starts ==================
platform darwin -- Python 3.6.3, pytest-3.4.2, py-1.5.2, pluggy-0.6.0
rootdir: /Users/taiker/workspace/new-flask-basic, inifile:
collected 6 items

tests/test_base.py ..                                                                                                                                           [ 33%]
tests/models/test_uesrs.py ....                                                                                                                                 [100%]

================ 6 passed in 5.78 seconds ================ 
```


## License

* MIT license
