import random
import secrets
from string import ascii_lowercase, ascii_uppercase, digits


class Codec:
    def __init__(self):
        self.hashmap = {}

    def _gen_key(self):
        n = random.randint(5, 8)
        key = "".join(
            secrets.choice(ascii_lowercase + ascii_uppercase + digits) for _ in range(n)
        )
        return key

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        key = self._gen_key()
        while key in self.hashmap:
            key = self._gen_key()

        self.hashmap[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.hashmap[shortUrl.split("/")[-1]]
