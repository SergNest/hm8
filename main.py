from datetime import datetime

from mongoengine import EmbeddedDocument, Document, CASCADE
from mongoengine.fields import (BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField,
                                IntField, ReferenceField)

import database.db


class User(Document):
    name = StringField()


class Page(Document):
    content = StringField()
    author = ReferenceField(User)


john = User(name="John Smith")
john.save()

post = Page(content="Test Page")
post.author = john
post.save()
