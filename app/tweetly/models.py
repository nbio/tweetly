from google.appengine.ext import db
from ragendja.auth.models import EmailUser

class User(EmailUser):
    first_name = db.StringProperty()
    last_name = db.StringProperty()

class Client(db.Model):
    name = db.StringProperty(required=True)
    user = db.ReferenceProperty(User)

class Delegate(db.Model):
    # key_name should be assigned when using the constructor
    pass

class Dogear(db.Model):
    item_id =  db.StringProperty(required=True)
    item_time = db.DateTimeProperty(auto_now_add=True)
    delegate = db.ReferenceProperty(Delegate)
    client = db.ReferenceProperty(Client)
