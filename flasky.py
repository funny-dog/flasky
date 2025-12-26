import os
import sys
import click
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)

@app.cli.command()
@click.option('--coverage/--no-coverage', default=False,
              help='Run tests under code coverage.')
@click.argument('test_names', nargs=-1)
def test(coverage, test_names):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        sys.exit(subprocess.call(sys.argv))

    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if coverage and os.environ.get('FLASK_COVERAGE'):
        # simple coverage report if needed, or rely on external tools
        print('Coverage run complete.')

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    from flask_migrate import upgrade
    upgrade()

    # create or update user roles
    Role.insert_roles()
    
    # ensure all users are following themselves
    User.add_self_follows()
