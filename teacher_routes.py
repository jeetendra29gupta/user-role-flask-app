from flask import Blueprint, render_template

from models import Role
from utils import login_required, role_required

teacher_router = Blueprint('teacher', __name__)


@teacher_router.route('/role-teacher')
@login_required
@role_required([
    Role.MATH_TEACHER.value,
    Role.ENGLISH_TEACHER.value,
    Role.SCIENCE_TEACHER.value,
    Role.HISTORY_TEACHER.value,
    Role.COMPUTER_TEACHER.value,
])
def role_teacher():
    return render_template('teacher_dashboard.html')
