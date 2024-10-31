from flask import Blueprint, render_template, request, flash, redirect, url_for, session

from database import Session
from models import User, Role
from utils import verify_password, login_required

router = Blueprint('router', __name__)


@router.route('/')
def index():
    return render_template('index.html')


@router.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username_or_email = request.form['username_or_email']
        password = request.form['password']

        with Session() as db:

            existing_user = db.query(User).filter(
                (User.username == username_or_email) | (User.email == username_or_email)
            ).first()

            if not existing_user:
                flash('Invalid username or email.', 'Error')
            elif not verify_password(password, existing_user.password):
                flash('Invalid password.', 'Error')
            else:
                session['username'] = existing_user.username
                session['email'] = existing_user.email
                session['is_active'] = existing_user.username
                session['role'] = existing_user.role.value
                flash('Login successful!', 'Success')
                return redirect(url_for('router.dashboard'))

    return render_template('login.html')


@router.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'Success')
    return redirect(url_for('router.login'))


@router.route('/dashboard')
@login_required
def dashboard():
    with Session() as db:
        user_role = session.get('role')
        data = None
        title = None

        if user_role == Role.PRINCIPAL.value:
            data = db.query(User).filter(User.role.in_([
                Role.MATH_TEACHER,
                Role.ENGLISH_TEACHER,
                Role.SCIENCE_TEACHER,
                Role.HISTORY_TEACHER,
                Role.COMPUTER_TEACHER,
            ])).all()
            title = "teachers"

        elif user_role in [
            Role.MATH_TEACHER.value,
            Role.ENGLISH_TEACHER.value,
            Role.SCIENCE_TEACHER.value,
            Role.HISTORY_TEACHER.value,
            Role.COMPUTER_TEACHER.value,
        ]:
            data = db.query(User).filter(User.role == Role.STUDENT).all()
            title = "students"

        elif user_role in Role.STUDENT.value:
            title = "marks"

    return render_template('dashboard.html', data=data, title=title)


@router.route('/profile')
@login_required
def profile():
    with Session() as db:
        username = session.get('username')
        existing_user = db.query(User).filter(User.username == username).first()
    return render_template('profile.html', data=existing_user)
