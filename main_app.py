import os

from dotenv import load_dotenv
from flask import Flask

from admin_routes import admin_router
from models import init_db
from routes import router
from student_routes import student_router
from teacher_routes import teacher_router

# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "Secret_Key-2024")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(router)
app.register_blueprint(admin_router)
app.register_blueprint(teacher_router)
app.register_blueprint(student_router)

with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8181, debug=True)
