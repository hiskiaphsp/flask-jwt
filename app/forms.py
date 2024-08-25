from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, ValidationError
from .models import User  # Pastikan Anda mengimpor model User dari tempat yang sesuai

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=150)])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long.'),
        Regexp('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', message='Password must contain both letters and numbers.')
    ])
    submit = SubmitField('Register')

    def validate_email(self, email):
        # Check if email already exists in the database
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different email address.')
