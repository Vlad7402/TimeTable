from flask import Flask, render_template, request, url_for, redirect, make_response, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    firstName = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    userType = db.Column(db.Integer, nullable=False)


class TimeTable(db.Model):
    __tablename__ = 'time_table'

    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(10), nullable=False)
    time_table = relationship("Weeks", back_populates="time_table")


class Weeks(db.Model):
    __tablename__ = 'weeks'

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Users %r>' % self.id


@app.route('/')
@app.route('/MainPage')
def mainpage():
    return render_template("MainPage.html")


@app.route('/CreateAccount', methods=['POST', 'GET'])
def CreateAcccount():
    users = User.query.order_by(User.id).all()
    if request.method == "POST":
        firstName = request.form['firstName']
        name = request.form['name']
        group = request.form['group']
        email = request.form['email']
        password = request.form['pass']
        userType = request.form['userType']
        if CheckEmailExist(email):
            return RenderCreateAccountPage(users, True, False)
        elif CheckGroupExist(group) and userType == "1":
            return RenderCreateAccountPage(users, False, True)
        else:
            user = User(firstName=firstName, name=name, group=group, email=email, password=generate_password_hash(password), userType=userType)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('SignIn'))
    else:
        return RenderCreateAccountPage(users, False, False)


@app.route('/SignIn', methods=['POST', 'GET'])
def SignIn():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']
        if email and password:
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user, True, datetime.timedelta(days=62))
                return redirect(url_for('TimeTable'))
            else:
                flash('Неправильный логин или пароль')
        else:
            flash('Все поля должны быть заполнены')
        return render_template("SignIn.html")
    else:
        return render_template("SignIn.html")


def CheckEmailExist(email):
    users = User.query.order_by(User.id).all()
    emails = []
    for user in users:
        emails.append(user.email)
    try:
        emails.index(email)
        return True
    except:
        return False


def CheckGroupExist(group):
    users = User.query.order_by(User.id).all()
    groups = []
    for user in users:
        groups.append(user.group)
    try:
        groups.index(group)
        return True
    except:
        return False


def RenderCreateAccountPage(users, is_email_exist, is_group_exist):
    groups = []
    for group in users:
        try:
            groups.index(group.group)
        except:
            groups.append(group.group)
    return render_template("CreateAccount.html", groups=groups, is_email_exist=is_email_exist, is_group_exist=is_group_exist)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('mainpage'))


@app.route("/TimeTable")
@login_required
def TimeTable():
    info = current_user.name + ", " + current_user.group
    flash("some text FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    return render_template("TimeTable.html", info=info)


@app.route("/TimeTableEdit", methods=['POST', 'GET'])
@login_required
def TimeTableEdit():
    if request.method == "POST":
        email = request.form['sn_p1_d1_week1']
        return redirect(url_for('TimeTable'))
    else:
        info = current_user.name + ", " + current_user.group
        week = ['Понедельник', 'Вторник', 'Среда', "Четверг", "Пятница", "Суббота", "Воскресенье"]
        week_counter = ['week1', 'week2']
        pair_num = ['1', '2', '3', "4", "5", "6", "7", "8"]
        return render_template("TimeTableEdit.html", info=info, week=week, week_counter=week_counter, pair_num=pair_num)


if __name__ == "__main__":
    app.secret_key = 'some secret key'
    app.run(debug=True)