import json


class PostEncoder(json.JSONEncoder):

    def default(self, obj):
        try:
            to_serialize = {
                'id': obj.id.hex,
                'text': obj.text,
                'timestamp': obj.timestamp.isoformat(), #strftime("%Y-%m-%d %H:%M:%S"),
                'created': obj.created.strftime("%Y-%m-%d %H:%M:%S"),
                'authorID': obj.author_id,
                'likesAmount': len(obj.likes),
                'likes': [
                    {
                        'authorID': like.author_id
                    } for like in obj.likes
                ],
            }
            return to_serialize
        except AttributeError as e:
            return super().default(obj)
