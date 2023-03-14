import hashlib


class Hasher:

    @staticmethod
    def get_image_hash(raw_image: bytes):
        sha256 = hashlib.sha256()
        sha256.update(raw_image)
        return sha256.hexdigest()
