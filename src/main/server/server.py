from flask import Flask
from src.main.routes.routes import user_rout_bp
app = Flask(__name__)

app.register_blueprint(blueprint= user_rout_bp)
