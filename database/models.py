from datetime import datetime

from mongoengine import EmbeddedDocument, Document, CASCADE
from mongoengine.fields import (BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField,
                                IntField, ReferenceField)

import database.db


class Tag(EmbeddedDocument):
    name = StringField()


class Record(EmbeddedDocument):
    description = StringField()
    done = BooleanField(default=False)


class Notes(Document):
    name = StringField()
    created = DateTimeField(default=datetime.now())
    records = ListField(EmbeddedDocumentField(Record))
    tags = ListField(EmbeddedDocumentField(Tag))
    meta = {'allow_inheritance': True}


class Cats(Document):
    name = StringField()
    age = IntField()
    features = ListField()


class Author(Document):
    fullname = StringField(unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()

