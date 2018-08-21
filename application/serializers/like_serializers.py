import json
from uuid import UUID


class LikeEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        try:
            print('in  like enc', obj)
            to_serialize = {
                'post_id': obj.post_id.hex,
                'author_id': obj.author_id
            }
            return to_serialize
        except AttributeError:
            return super().default(obj)
