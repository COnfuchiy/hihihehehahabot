import requests
from PIL import Image
from dependency_injector.wiring import Provide, inject
from io import BytesIO
from requests import RequestException

from src.image.entity import ImageObject
from src.utils.hasher import Hasher
from src.utils.logger import GeneralLogger


class ImageReceiver:

    @inject
    def __init__(self, logger: GeneralLogger = Provide['logger']):
        self._logger = logger

    def from_url(self, url: str) -> ImageObject:
        try:
            response = requests.get(url, stream=True)
            image = Image.open(response.raw)
            image_as_bytes_array = BytesIO()
            image.save(image_as_bytes_array, format='PNG')
            image_hash = Hasher.get_image_hash(
                image_as_bytes_array.getvalue())
            return ImageObject(
                image=image,
                hash=image_hash
            )
        except RequestException:
            self._logger.image_request_error()
