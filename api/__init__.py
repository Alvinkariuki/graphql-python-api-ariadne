from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mkqfcgdr:LXA-rO3gkrtirLVDpqVRUXhq1fggXSl6@fanny.db.elephantsql.com/mkqfcgdr"
app.config["SQL_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My first Graphql API'