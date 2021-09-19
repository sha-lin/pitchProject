from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField("Pitch Title")
    category = SelectField(u"Pitch Category",choices=[("interview", "interview"),("funny","funny"),("promotion","promotion"),("product","product"),("random","random")])
    pitch = TextAreaField('Pitch')
    submit = SubmitField("Submit")

# add comment

class CommentForm(FlaskForm):
    
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')

# update profile

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')