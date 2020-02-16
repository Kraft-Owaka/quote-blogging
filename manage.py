# from flask import Flask
from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User

app=create_app('development')
app=create_app('production')
manager = Manager(app)

manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(db = db, app = app, User = User, Post = Post, Pitch = pitch, Upvote = upvote, Downvote = downvote, Comment = comment)
    
if __name__ == '__main__':
    manager.run()