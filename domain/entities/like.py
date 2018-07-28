from uuid import uuid4


class Like(object):
    def __init__(self, post_id: uuid4(), author_id: uuid4()):
        self.post_id = post_id
        self.author_id = author_id
