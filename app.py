import os
from flask import Flask 
from src.database import DB
from src.routes import mobile_route

project_root = os.path.dirname(__file__)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'shambala'

DB.init()

app.debug = True

app.register_blueprint(mobile_route.get_blueprint(), url_prefix="/mobile")

if __name__ == "__main__":
   app.run()