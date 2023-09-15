from flask import Blueprint, render_template, request
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


@views.route('/')
def home():
    test = 'welcome'
    return render_template("Home.html", user=current_user)


@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    print('before')
    if request.method == 'POST':
        print('hello')
        file = request.files['file']
        print(file)

    return render_template("user_dashboard.html", user=current_user)
