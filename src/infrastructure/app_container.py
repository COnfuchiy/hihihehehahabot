from dependency_injector import containers, providers

from src.image.service import ImageService
from src.telegram.service import TelegramService
from src.utils.logger import GeneralLogger
from src.vk.api.service import VKService


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    logger = providers.Singleton(
        GeneralLogger,
    )

    vk_service = providers.Singleton(
        VKService,
    )

    image_service = providers.Singleton(
        ImageService
    )

    telegram_service = providers.Singleton(
        TelegramService
    )
