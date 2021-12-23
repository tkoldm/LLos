from flask import Flask
from flask_migrate import Migrate

from config import Config
from Models.StudenModel import Student, db
from Application.Controller.StudentController import student_blueprint

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(student_blueprint)
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()