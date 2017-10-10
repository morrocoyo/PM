import datetime
import mongoengine
from mongoengine import *
from PrimerMongo import DBNAME

# User = settings.AUTH_USER_MODEL
# User = User

# Create your models here.

mongoengine.connect(DBNAME)

class BlogPost(Document):
    title       = StringField(max_length=120,required=True)
    content     = StringField(max_length=500, required=True)
    last_update = DateTimeField(default=datetime.datetime.utcnow,required=True)
    meta = {
        'allow_inheritance': True
    }
