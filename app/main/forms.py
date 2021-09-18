from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, SelectField, FileField
from wtforms.validators import Required

class AddPitch(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    pitch = TextAreaField("Description", validators = [Required()])
    category = SelectField(
        "category",
        choices=[("interview", "interview"),("funny","funny"),("promotion","promotion"),("product","product"),("random","random")],validators = [Required()]
    )
    submit = SubmitField("Add pitch")

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')