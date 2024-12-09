from flask import Flask
from flask_sqlalchemy import SQLAchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
