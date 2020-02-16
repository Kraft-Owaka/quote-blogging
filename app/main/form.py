from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required




class PitchForm(FlaskForm):

    title=StringField('Pitch title', validators=[Required()])
    category=RadioField('Label',choices=[('investorpitch','investorpitch'),('productpitch','productpitch'),('interviewpitch','interviewpitch'),('marketpitch','marketpitch')],validators=[Required()])
    content=TextAreaField('Enter your pitch', validators=[Required()])
    submit=SubmitField('Submit')
    

class CommentForm(FlaskForm):
    description=TextAreaField('Leave a comment')
    comment = TextAreaField('comment', validators=[Required()])
    submit=SubmitField()

class UpvoteForm(FlaskForm):
    submit=SubmitField()

class DownvoteForm(FlaskForm):
    submit=SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please describe yourself',validators = [Required()])
    submit = SubmitField('Update')

