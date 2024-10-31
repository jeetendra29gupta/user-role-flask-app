from flask import Blueprint, render_template, request, flash, redirect, url_for

from database import Session
from models import User, Role
from utils import hash_password
from utils import login_required, role_required

admin_router = Blueprint('admin', __name__)


@admin_router.route('/add-teacher', methods=['GET', 'POST'])
@login_required
@role_required([Role.PRINCIPAL.value])
def add_teacher():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        role = request.form['role']
        if not role in [role.name for role in Role]:
            flash('Invalid role selected. Please choose a valid role.', 'Error')
        else:
            with Session() as db:
                existing_user_by_username = db.query(User).filter(User.username == username).first()
                existing_user_by_email = db.query(User).filter(User.email == email).first()

                if existing_user_by_username:
                    flash('User with this username already exists.', 'Error')
                elif existing_user_by_email:
                    flash('User with this email already exists.', 'Error')
                else:
                    new_user = User(
                        username=username,
                        email=email,
                        password=hash_password(password),
                        role=role
                    )

                    db.add(new_user)
                    db.commit()
                    flash('Teacher added successfully!', 'Success')
                    return redirect(url_for('router.dashboard'))

    return render_template('add-teacher.html', role=[role.name for role in Role])


@admin_router.route('/role-principal')
@login_required
@role_required([Role.PRINCIPAL.value])
def role_principal():
    return render_template('principal_dashboard.html')
