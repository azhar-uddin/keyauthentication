from flask import Blueprint, g, jsonify, render_template, flash, redirect, url_for, request
from app.models.user import User

WEB_BP = Blueprint('web', __name__, url_prefix='', template_folder='templates')

@WEB_BP.route('/')
@WEB_BP.route('/users')
def index():
	users = User.find_all()
	if len(users) == 0:
		flash("No Users found", 'warning')
	return render_template('users/index.html', users=users)

@WEB_BP.route('/users/new')
def new_user():
	return render_template('users/new_user.html')


@WEB_BP.route('/users/new',methods = ['POST', 'GET'])
def create_user():
	try:
		user = User(
			email = request.form['emailInput'],
			name = request.form['nameInput'],
			company = request.form['companyInput'],
			phone = request.form['phoneInput'],
			password = request.form['passwordInput']
		)
		user.save()
		flash('You have successfully created a new User.', "success")
		return redirect(url_for('web.index'))
	except Exception as ex:
		flash("User with the Email or Phone number already exists", "danger")
		return redirect(url_for('web.index'))

@WEB_BP.route('/users/<id>/edit')
def edit_user(id):
	user = User.find_by_id(id)
	return render_template('users/edit_user.html', user=user)


@WEB_BP.route('/users/<id>/update',methods = ['POST', 'GET'])
def update_user(id):
	try:
		user = User.find_by_id(id)
		if user.verify_password(request.form['passwordInput']):
			user.email = request.form['emailInput'],
			user.name = request.form['nameInput'],
			user.company = request.form['companyInput'],
			user.phone = request.form['phoneInput']
			user.save()
			flash('User updated successfully.', "success")
			return redirect(url_for('web.index'))
		else:
			flash('Wrong Password', "danger")
			return render_template('users/edit_user.html', user=user)
	except Exception as ex:
		flash("User with the Email or Phone number already exists", "danger")
		return redirect(url_for('web.index'))


@WEB_BP.route('/delete/<id>')
def delete_user(id):
	user = User.find_by_id(id)
	user.delete()
	flash('You have successfully deleted the User.', "success")
	return redirect(url_for('web.index'))
