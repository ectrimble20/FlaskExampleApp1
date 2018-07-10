from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class ForumCreate(FlaskForm):
    end_point = StringField("Tag", validators=[DataRequired(), Length(max=45)])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create New Forum')


class ForumEdit(FlaskForm):
    end_point = StringField("Tag", validators=[DataRequired(), Length(max=45)])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Update Forum')
