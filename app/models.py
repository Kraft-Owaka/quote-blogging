from . import db
from datetime import datetime
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())
    pass_secure=db.Column(db.String(255))
    post=db.relationship('Post', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
  

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'{self.username}'
        ''
    @staticmethod
    def verify_reset_token(token):
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Pitch(db.Model):
    __tablename__ =  'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow )
    content = db.Column(db.String(255), nullable = False)
    category = db.Column(db.String(255), nullable= False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
    


    def __repr__(self):
        return f"Pitch('{self.title}','{self.date_posted}','{self.content}')"
    
    @classmethod
    def get_pitches(cls,owner_id):
        pitches = Pitch.query.filter_by(owner_id=owner_id)
        return pitches
    @classmethod
    def get_all_pitches(cls):
        pitch=Pitch.query.all()
        return pitch


class Comment(db.Model):

    __tablename__='comments'

    id =db.Column(db.Integer,primary_key=True)
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable=False)
    post=db.Column(db.String(255),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
    description=db.Column(db.Text)

    def __repr__(self):
        return f'Comment: id: {self.id} comment: {self.description}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_upvotes(cls,id):
        upvote_pitch = Upvote(user = current_user, pitch_id=id)
        upvote_pitch.save_upvotes()

    
    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote

    @classmethod
    def get_all_upvotes(cls,pitch_id):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    downvote = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_downvotes(cls,id):
        downvote_pitch = Downvote(user = current_user, pitch_id=id)
        downvote_pitch.save_downvotes()

    
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote

    @classmethod
    def get_all_downvotes(cls,pitch_id):
        downvote = Downvote.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
