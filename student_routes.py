from flask import Blueprint, render_template

from models import Role
from utils import login_required, role_required

student_router = Blueprint('student', __name__)


@student_router.route('/role-student')
@login_required
@role_required([Role.STUDENT.value])
def role_student():
    return render_template('student_dashboard.html')
