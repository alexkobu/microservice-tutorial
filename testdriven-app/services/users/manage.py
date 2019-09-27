# services/users/manage.py

from flask.cli import FlaskGroup

from project import app, db

cli = FlaskGroup(app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    deb.session.commit()

if __name__ == '__main__': 
    cli()