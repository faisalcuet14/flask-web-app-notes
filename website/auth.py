from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

# @route /login 
# @access public
# @desc login route
@auth.route('/login')
def login():
    return render_template("login.html")

# @route /logout 
# @access private
# @desc logout route
@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

# @route /signup 
# @access public
# @desc signup route
@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # print(request.form)
        data = {
            'email' : request.form.get('email'),
            'name' : request.form.get('name'),
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
            flash('Account created', category='success')
    return render_template('sign_up.html')
