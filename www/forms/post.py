from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length


class NewPostForm(FlaskForm):
    forum_id = HiddenField('forum_id')
    title = StringField('Title', validators=[DataRequired(), Length(max=120)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit New Post')


class EditPostForm(FlaskForm):
    body = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('Edit Post')


class ReplyPostForm(FlaskForm):
    post_id = HiddenField('post_id')
    body = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('Submit Reply')

