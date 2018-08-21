from datetime import datetime

from mongoengine import Document, EmbeddedDocument, StringField, DateTimeField, \
    ListField, EmbeddedDocumentField, connect

connect('test2')


class Like(EmbeddedDocument):
    post_id = StringField()
    author_id = StringField()


class Post(Document):
    text = StringField(required=True)
    timestamp = DateTimeField(default=datetime.utcnow)
    created = DateTimeField(default=datetime.utcnow)
    author_id = StringField(required=True)
    likes = ListField(EmbeddedDocumentField(Like))
