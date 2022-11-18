from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('loginRegister.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    data={
        'name':request.form['name'],
        'lastName':request.form['lastName'],
        'email':request.form['email'],
    }
    User.create_user(data)
    return redirect('/profilePage')

@app.route('/profilePage')
def profile():
    allUser = User.getAllUsers()
    return render_template ('profilePage.html', users = allUser)



@app.route('/delete/<int:id>')
def deleteuser(id):
    data={
        'id':id
    }
    User.delete_user(data)
    return redirect('/profilePage')


@app.route('/users/<int:id>')
def showuser(id):
    data={
        'id':id
    }
    user= User.get_user_by_id(data)
    return render_template('data.html',user=user)

@app.route('/users/<int:id>/edit')
def edit(id):
    data={
        'id':id
    }
    user= User.get_user_by_id(data)
    return render_template('users_data_edit.html',user=user)


@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data={
        'name':request.form['name'],
        'lastName':request.form['lastName'],
        'email':request.form['email'],
        'id':id
    }
    User.update_user(data)
    return redirect('/users/'+str(id))

@app.route('/home')
def home():
    return render_template('profilePage.html')