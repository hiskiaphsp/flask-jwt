from flask_jwt_extended import create_access_token

def create_token(user):
    return create_access_token(identity=user.id)

def verify_password(user, password):
    return user.check_password(password)
