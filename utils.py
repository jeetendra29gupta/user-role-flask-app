from datetime import datetime
from functools import wraps
from typing import Callable, List, Any

import bcrypt
from flask import session, redirect, url_for, flash

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def hash_password(password: str) -> str:
    """Hash a password using bcrypt.

    Args:
        password (str): The plain text password.

    Returns:
        str: The hashed password.

    Raises:
        ValueError: If the password is empty or hashing fails.
    """
    try:
        if not password:
            raise ValueError("Password cannot be empty")
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    except Exception as e:
        raise ValueError(f"An error occurred while hashing the password: {e}")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain text password against a hashed password.

    Args:
        plain_password (str): The plain text password.
        hashed_password (str): The hashed password.

    Returns:
        bool: True if the password matches, otherwise False.

    Raises:
        ValueError: If the hashed password is invalid or verification fails.
    """
    try:
        if not hashed_password:
            raise ValueError("Hashed password cannot be empty")
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        raise ValueError(f"An error occurred while verifying the password: {e}")


def login_required(fun: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to check if a user session exists.

    If the user is not logged in, they will be redirected to the login page with an error message.

    Args:
        fun (Callable[..., Any]): The function to be wrapped.

    Returns:
        Callable[..., Any]: The wrapped function or redirect.
    """

    @wraps(fun)
    def decorated_function(*args, **kwargs) -> Any:
        try:
            # Check if user is logged in by looking for session data
            if 'username' not in session:
                flash('Invalid session. Please log in again.', 'Error')
                return redirect(url_for('router.login'))  # Redirect to login route
            return fun(*args, **kwargs)  # User is logged in, proceed to the requested function
        except Exception as e:
            # Log the error or handle it as needed
            flash('An error occurred while checking session: {}'.format(e), 'error')
            return redirect(url_for('router.login'))  # Redirect to login route on error

    return decorated_function


def role_required(allowed_roles: List[str]) -> Callable:
    """Decorator to ensure the user has the required role.

    If the user does not have the required role, they will be redirected to a safe page with an error message.

    Args:
        allowed_roles (List[str]): A list of roles that are allowed to access the function.

    Returns:
        Callable[..., Any]: The wrapped function or redirect.
    """

    def decorator(fun: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(fun)
        def decorated_function(*args, **kwargs) -> Any:
            try:
                if 'role' not in session or session['role'] not in allowed_roles:
                    flash('You do not have permission to access this page.', 'Error')
                    return redirect(url_for('router.login'))  # Redirect to a safe page
                return fun(*args, **kwargs)  # User has the required role, proceed to the requested function
            except Exception as e:
                # Log the error or handle it as needed
                flash('An error occurred while checking user role: {}'.format(e), 'Error')
                return redirect(url_for('router.login'))  # Redirect to a safe page on error

        return decorated_function

    return decorator
