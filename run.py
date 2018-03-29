from src.models import users
from src import app, db
from flask import url_for
import urllib
import click

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
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == '__main__':
    app.run()
