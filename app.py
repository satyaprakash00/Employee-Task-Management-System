from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from models.database import db

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-for-testing')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///task_management.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Import models
from models.user import User
from models.task import Task

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

# Register blueprints
def register_blueprints():
    from routes.auth import auth_bp
    from routes.tasks import tasks_bp
    from routes.chat import chat_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(chat_bp)

# Initialize the app
def init_app():
    with app.app_context():
        register_blueprints()
        db.create_all()

if __name__ == '__main__':
    init_app()
    app.run(debug=True)