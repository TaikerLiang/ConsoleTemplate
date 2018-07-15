"""
.. module:: run
   :platform: Ubuntu 16.04 & Mac OS
   :synopsis: Main function of flask service

.. moduleauthor:: Paul Liang <liang0816tw@gmail.com>
.. date:: 2018-03-29
"""

from src.models import users
from src import app, db
from flask import url_for
from config import config
import urllib
import click
import sys
import getopt
import os


@app.cli.command()
def new_user():
    user = users.User('paul', 'paul@email.com', 'paul@password')
    db.session.add(user)
    db.session.commit()


@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')
    db.create_all()


@app.cli.command()
def renewdb():
    """Remove the database."""
    click.echo('Renew the db')
    db.drop_all()
    db.create_all()


@app.cli.command()
def list_routes():
    """List all routes on flask service"""
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.unquote(
                "{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == '__main__':
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "hcf", ["help", "ci", "front-end"])
    except getopt.GetoptError:
        print('please type: python3 run.py -h to help you')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('usage: python3 run.py [COMMAND] ')
            print('COMMAND:')
            print('\t -c --ci: for ci mode')
            print('\t -f --front-end: for front-end mode')
            sys.exit()
        elif opt in ("-c", "--ci"):
            print("CI mode")
            app.config.from_object(config['development'])
        elif opt in ("-f", "--front-end"):
            print("front-end mode")
            app.config.from_object(config['testing'])
            click.echo('Renew the db')
            db.drop_all()
            db.create_all()
            user = users.User('paul', 'paul@email.com', 'paul@password')
            db.session.add(user)
            db.session.commit()
    app.run()
