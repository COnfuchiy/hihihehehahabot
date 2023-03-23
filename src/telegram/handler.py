import json

from dependency_injector.wiring import Provide, inject

from src.image.service import ImageService
from src.telegram.service import TelegramService
from src.utils.logger import GeneralLogger


class TelegramHandler:
    @inject
    def __init__(
            self,
            logger: GeneralLogger = Provide['logger'],
            telegram_service: TelegramService = Provide['telegram_service'],
            image_service: ImageService = Provide['image_service']):
        self._logger = logger
        self._telegram_service = telegram_service
        self._image_service = image_service

    def handle_photo_receiving(self, json_data: str):
        try:
            image_data = json.loads(json_data)
            if not image_data and not len(image_data):
                return
            max_size_image_id = TelegramHandler.get_max_size_image_file_id(
                image_data)
            if max_size_image_id:
                image_url = self._telegram_service.get_url_file(
                    max_size_image_id)
                _ = self._image_service.get_image_from_url(image_url)
        except (ValueError,):
            self._logger.telegram_image_converting()

    @staticmethod
    def get_max_size_image_file_id(file_sizes) -> str:
        max_height = 0
        max_size_file_id = ''
        for size in file_sizes:
            current_height = size.get('height', 0)
            if current_height > max_height:
                max_height = current_height
                max_size_file_id = size.get('file_id', '')
        return max_size_file_id
