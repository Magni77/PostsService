import json
import uuid
from datetime import datetime
from uuid import uuid4, UUID

import inject
from bottle import route, run, response, request

from api.decorators import login_required
from application.repositories.memory_posts import MemoryPostsRepository
from application.repositories.mongo_posts import MongoPostsRepository
from application.repositories.posts import PostsRepository
from application.serializers.post_serializers import PostEncoder
from application.use_cases.like_post_use_case import LikePostUseCase
from application.use_cases.post_use_cases import PostListUseCase, CreatePostUseCase


def config(binder):
    binder.bind(PostsRepository, MemoryPostsRepository())


inject.configure(config)

id1 = uuid4()
id2 = uuid4()

post_data = dict(
        id=id1,
        text="tefdsfsst",
        timestamp=datetime(1995, 2, 22, 16, 5),
        created=datetime(1995, 2, 22, 16, 6),
        author_id="4b114b4315b24df09829e0bd2ab4a89f"
    )

post_data2 = dict(
        id=id2,
        text="tefdsf32sst",
        timestamp=datetime(1995, 2, 22, 16, 5),
        created=datetime(1995, 2, 22, 16, 6),
        author_id="4b114b4315b24df09829e0bd2ab4a89f"
    )

create_post = CreatePostUseCase().create(post_data)
create_post2 = CreatePostUseCase().create(post_data2)

posts = PostListUseCase().get_list({})

post1 = PostListUseCase().get_list({'author_id': "4b114b4315b24df09829e0bd2ab4a89f"})[0].to_dict()

LikePostUseCase().like_post(post1['id'], 1)


@route('/posts')
@login_required
def posts(user):
    response.headers['Content-Type'] = 'application/json'
    filter_params = request.query.decode()
    posts = PostListUseCase().get_list(filter_params)
    return json.dumps([post for post in posts], cls=PostEncoder)


@route('/posts', method='POST')
@login_required
def create_post(user):
    response.headers['Content-Type'] = 'application/json'
    use_case = CreatePostUseCase()
    request.json['author_id'] = user.get('id')
    post = use_case.create(request.json)

    return json.dumps(post, cls=PostEncoder)


@route('/posts/<id>/like', method='PUT')
@login_required
def posts(user, id):
    response.headers['Content-Type'] = 'application/json'
    post = LikePostUseCase().like_post(uuid.UUID(id), user.get('id'))

    return json.dumps(post, cls=PostEncoder)


run(host='localhost', port=8082, debug=True, reloader=True)
