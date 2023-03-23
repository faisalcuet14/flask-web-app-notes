from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# @route /login 
# @access public
# @desc login route
@auth.route('/login')
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

# @route /logout 
# @access private
# @desc logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# @route /signup 
# @access public
# @desc signup route
@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # print(request.form)
        data = {
            'name' : request.form.get('name'),
            'email' : request.form.get('email'),
            'password' : request.form.get('password'),
            'confirmPassword' : request.form.get('confirmPassword')
        }
        # print(data)
        if data['email'] == '' or data['name'] == '' or data['password'] == '' or data['confirmPassword'] == '':
            flash('All fileds are required', category='error')
        elif data['password'] != data['confirmPassword']:
            flash('Passwords don\'t match', category='error')
        elif len(data['password']) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # handle new account creation
            new_user = User(name=data['name'], email=data['email'],password=generate_password_hash(data['password'], method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
    return render_template('sign_up.html')
