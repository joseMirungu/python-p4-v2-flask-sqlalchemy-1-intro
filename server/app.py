from flask import Flask
from flask_migrate import Migrate
from models import db, Pet

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize migration
migrate = Migrate(app, db)

# Initialize the database
db.init_app(app)

# Define a simple route to test the application
@app.route('/')
def home():
    return 'Flask App is Running'

if __name__ == '__main__':
    app.run(port=5555)
