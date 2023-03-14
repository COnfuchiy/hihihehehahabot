import telebot
from dependency_injector.wiring import Provide, inject
from telebot.apihelper import ApiException

from src.image.entity import ImageObject
from src.utils.logger import GeneralLogger


class TelegramService:

    @inject
    def __init__(self,
                 logger: GeneralLogger = Provide['logger'],
                 api_token: str = Provide['config.tg.api_access_token'],
                 chat_id: str = Provide['config.tg.chat_id']):
        self._logger = logger
        self._api_token = api_token
        self._chat_id = chat_id
        self._bot = self._init_session()

    def _init_session(self) -> telebot.TeleBot:
        try:
            return telebot.TeleBot(token=self._api_token)
        except (Exception,):
            self._logger.telegram_setup_error()

    def send_image(self, image_object: ImageObject, text: str = ''):
        try:
            self._bot.send_photo(
                chat_id=self._chat_id,
                photo=image_object.image_to_bytes(),
                caption=text)
        except (ApiException, Exception):
            self._logger.telegram_setup_error()
