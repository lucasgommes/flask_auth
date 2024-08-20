from flask import Blueprint, jsonify, render_template, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


bp = Blueprint('app', __name__, template_folder='../templates')

@bp.route('/')
def home_page():
    return render_template('index.html')


@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token = access_token)


@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
