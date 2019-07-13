from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class BlogForm(Form):
    title = StringField(
        "title",
        validators=[
            DataRequired(
                message="Blog title is required."
            )
        ]
    )
    content = TextAreaField(
        "content",
        validators=[
            DataRequired(
                message="Blog content is required."
            )
        ]
    )