from flask import Flask
from flask import jsonify
from flask import request
from controllers.auth_user import bp

from flask_jwt_extended import JWTManager


app = Flask(__name__)

# Resgister blueprint
app.register_blueprint(bp)


app.config["JWT_SECRET_KEY"] = "super-secret"
jet = JWTManager(app)


if __name__ == "__main__":
    app.run(debug=True)