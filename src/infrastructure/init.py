from dependency_injector.wiring import Provide, inject

from src.image.service import ImageService
from src.telegram.handler import TelegramHandler
from src.telegram.service import TelegramService
from src.utils.logger import GeneralLogger
from src.vk.api.service import VKService


@inject
def run_app(
        max_get_image_iteration: int = Provide['config.max_get_image_iteration'],
        logger: GeneralLogger = Provide['logger'],
        vk_service: VKService = Provide['vk_service'],
        image_service: ImageService = Provide['image_service'],
        telegram_service: TelegramService = Provide['telegram_service']):
    for _ in range(0, max_get_image_iteration):
        post = vk_service.get_random_post_with_attachments()
        for attachment in post.attachments:
            image = image_service.get_image_from_url(attachment.url)
            if image:
                telegram_service.send_image(
                    image, VKService.get_message_to_image(
                        post.group_name, post.text))
                return
    logger.max_iteration_image_search_reached()
    raise SystemExit()


@inject
def run_telegram_handler(
        json_data: str = '',
        telegram_handler: TelegramHandler = Provide['telegram_handler']):
    if json_data:
        telegram_handler.handle_photo_receiving(json_data)
