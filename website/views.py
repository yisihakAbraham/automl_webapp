from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


@views.route('/')
def home():
    test = 'welcome'
    return render_template("Home.html", user=current_user)


@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("user_dashboard.html", user=current_user)
