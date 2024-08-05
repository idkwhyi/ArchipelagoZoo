from flask import Flask
from flask_sqlalchemy import SQLAlchemy #type: ignore
from flask_cors import CORS


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/ArchipelagoZoo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Automaticly creating the models
    with app.app_context():
      from .models import User, Animal
      db.create_all()

    # Register Blueprints
    from .routes.auth_routes import auth # auth blueprint
    from .routes.animal_routes import animals # auth blueprint

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(animals, url_prefix='/animals')

    return app


# ! TO CALL THE ROUTES
'''
/auth/login
/auth/register

....etc
'''