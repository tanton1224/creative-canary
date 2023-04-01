from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, TimeField, BooleanField
from wtforms.validators import DataRequired


class LessonForm(FlaskForm):
    client_id = IntegerField("Client ID", validators=[DataRequired()])
    date = DateField("Date", format='%Y-%m-%d', validators=[DataRequired()])
    start_time = TimeField("Start Time", format='%H:%M', validators=[DataRequired()])
    end_time = TimeField("End Time", format='%H:%M', validators=[DataRequired()])
    client_name = StringField("Client Name", validators=[DataRequired()])
    approved = BooleanField("Approved")
