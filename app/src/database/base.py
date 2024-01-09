import json
from uuid import uuid4

class RedisSession:
    def __init__(self, redis, prefix=None):
        self.redis = redis
        self.prefix = prefix

    def _keys(self, pattern="*"):
        return [self._get(key) for key in self.redis.keys(pattern)]

    def _get(self, key, default=None):
        data = self.redis.get(key)

        if data is None:
            return default

        value = json.loads(data)

        if value is None:
            return default

        return value

    def _set(self, key, value):
        data = json.dumps(value)
        self.redis.set(key, data)

    def _delete(self, key):
        self.redis.delete(key)

    def _setex(self, key, value, expiry: int):
        data = json.dumps(value)
        self.redis.setex(key, expiry, data)

    def _close(self):
        self.redis.close()



class DbItem(RedisSession):
    def all(self):
        return self._keys(pattern=f"{self.prefix}:*")

    def get(self, uid):
        return self._get(f"{self.prefix}:{uid}")


    def add(self, item: dict):
        item["id"] = str(uuid4())
        self._set(f"{self.prefix}:{item["id"]}", item)

    def update(self, item: dict):
        if not item.get("id"):
            raise ValueError("No id provided")
        self._set(f"{self.prefix}:{item.get("id")}", item)

    def delete(self, item: dict):
        self._delete(f"{self.prefix}:{item.get("id")}")
