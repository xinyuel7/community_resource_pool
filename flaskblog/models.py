from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):#donator
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)#many posts to 1 user relationship
#backref -- add a column(the entire user object) to the Post model 
#lazy when SQLachemy will load the data from the database in one go
#we can't see the post column in User model, instead running an additional query in the background that will get all of the posts this user has created
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):#the item to be donated
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    picture = db.Column(db.String(20), nullable=False, default='default.jpg')
    #category = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.picture}')"
