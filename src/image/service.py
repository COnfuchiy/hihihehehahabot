from dependency_injector.wiring import Provide, inject

from src.image.entity import ImageObject
from src.image.receiver import ImageReceiver
from src.image.register import ImageRegister
from src.utils.logger import GeneralLogger


class ImageService:

    @inject
    def __init__(self,
                 logger: GeneralLogger = Provide['logger']):
        self._logger = logger
        self._image_register = ImageRegister()
        self._image_receiver = ImageReceiver()

    def get_image_from_url(self, image_url: str) -> ImageObject:
        image_object = self._image_receiver.from_url(image_url)
        if not image_object:
            return None
        if not self._image_register.check_image_hash_existing(image_object):
            self._image_register.add_hash(image_object)
            return image_object
