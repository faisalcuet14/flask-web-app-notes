from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# @route GET /
# @access private
# @desc homepage, create and delete notes

@views.route('/')
def home():
  return render_template('index.html')