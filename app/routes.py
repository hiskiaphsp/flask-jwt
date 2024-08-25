from flask import Blueprint, request, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User
from . import db
from .services.auth_service import create_token
from .response import success_response, error_response
from .forms import RegistrationForm

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/register', methods=['POST'])
def register():
    form = RegistrationForm(data=request.get_json())
    if not form.validate():
        return error_response(
            message="Validation failed",
            error=form.errors,
            status=400
        )

    if User.query.filter_by(email=form.email.data).first():
        return error_response(message="Registration failed", error="Email already exists.", status=400)

    user = User(name=form.name.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()

    return success_response(data={"user": {"name": user.name, "email": user.email}}, message="User registered successfully", status=201)

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return error_response(message="Login failed", error="Email and password are required.", status=400)

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return error_response(message="Login failed", error="Invalid credentials.", status=401)

    access_token = create_token(user)
    return success_response(data={"access_token": access_token}, message="Login successful", status=200)

@api_bp.route('/user-info', methods=['GET'])
@jwt_required()
def user_info():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return error_response(message="User not found", error="No user exists with the provided token", status=404)

    user_data = {
        "name": user.name,
        "email": user.email
    }

    return success_response(data={"user": user_data}, message="User information retrieved successfully", status=200)

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/login', methods=['GET'])
def show_login():
    return render_template('login.html')

@frontend_bp.route('/register', methods=['GET'])
def show_register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

@frontend_bp.route('/home', methods=['GET'])
def show_home():
    return render_template('home.html')
