from initApp import db
import datetime

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_from_web_id = db.Column(db.Integer, db.ForeignKey('user_database_from_web.user_id'))
    user_line_id = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50),nullable=False)
    status = db.Column(db.String(10))
    projects = db.relationship('CreateProject',backref="user")
    otp = db.Column(db.String(10))
    otp_expireTime = db.Column(db.DateTime)  
    last_activity_time = db.Column(db.DateTime, default=datetime.datetime.now())
    last_login_time = db.Column(db.DateTime, default=datetime.datetime.now())
    def __repr__(self):
        return f"user('{self.name}')"

class CreateProject(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    project_owner = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    project_name = db.Column(db.String(60), nullable=False)
    project_price = db.Column(db.Float, nullable=False)
    project_create_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    project_description = db.Column(db.String(200))
    project_lastedit_time = db.Column(db.DateTime, default=datetime.datetime.now())
    # def __repr__(self):
    #     return '<User %r>' % self.username

    # def __init__(self, name, price,description=None):
    #     self.project_name = name
    #     self.project_price = price
    #     self.project_description= description  

class userDatabase_fromWeb(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))
    users = db.relationship("User",backref="user_database_from_web")

