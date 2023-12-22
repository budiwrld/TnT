from flask import Flask
from flask_bcrypt import Bcrypt
from config import ApplicationConfig, db

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
bcrypt = Bcrypt(app)

with app.app_context():
    db.init_app(app)
    db.create_all()

from auth import auth
app.register_blueprint(auth, url_prefix='/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)