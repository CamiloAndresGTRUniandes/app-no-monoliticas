from config.db import db
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:LosAndes1234@{os.getenv('DATABASE_HOST', default='127.0.0.1')}:5432/properties"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
