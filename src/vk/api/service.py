import random

from dependency_injector.wiring import Provide, inject

from src.utils.logger import GeneralLogger
from src.vk.api.session import VKSession
from src.vk.domain.dto.post import PostDto
from src.vk.domain.entity.post import Post
from src.vk.domain.mapper.post import PostMapper


class VKService:
    _max_wall_request_offset = 100
    _max_request_iteration = 30
    _max_get_image_iteration = 30

    @inject
    def __init__(
            self,
            vk_domain_list: list = Provide['config.vk.domain_list'],
            logger: GeneralLogger = Provide['logger']):
        self._logger = logger
        self._vk_domain_list = vk_domain_list
        self._session = VKSession()

    def get_random_post_with_attachments(self) -> Post:
        for _ in range(0, self._max_request_iteration):
            random_domain = random.choice(self._vk_domain_list)
            random_offset = random.randint(1, self._max_wall_request_offset)
            posts_data = self._session.get_wall_posts(
                random_domain, 1, random_offset)
            if 'items' in posts_data and len(posts_data['items']):

                # for one first post
                post_data = posts_data['items'][0]
                if not VKService.filter_post_data(post_data):
                    continue
                post_dto = PostDto.from_dict(post_data)
                post = PostMapper.to_entity(post_dto)
                if post:
                    return post
        self._logger.max_iteration_post_search_reached()
        raise SystemExit()

    @staticmethod
    def filter_post_data(post_data: dict) -> bool:
        try:
            return True if post_data['marked_as_ads'] != 1 \
                           and not post_data['donut']['is_donut'] else False
        except KeyError:
            return False
