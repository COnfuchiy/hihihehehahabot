from time import sleep

import vk
from dependency_injector.wiring import Provide
from vk.exceptions import VkAPIError

from src.utils.logger import GeneralLogger


class VKSession:
    def __init__(self,
                 logger: GeneralLogger = Provide['logger'],
                 api_key: str = Provide['config.vk.api_access_token'],
                 api_version: str = Provide['config.vk.api_version']):
        self._logger = logger
        self._api_key = api_key
        self._api_version = api_version
        self._session = self._init_session()

    def _init_session(self):
        try:
            return vk.API(access_token=self._api_key, v=self._api_version)
        except (Exception,):
            self._logger.vk_api_setup_error()
            raise SystemExit()

    def get_wall_posts(
            self,
            domain: str,
            posts_count: int = 1,
            offset: int = 1) -> dict:
        try:
            sleep(0.3)
            return self._session.wall.get(
                domain=domain, count=posts_count, offset=offset)
        except VkAPIError as exception:
            if not exception.code == 0:
                self._logger.vk_api_request_error()
            raise SystemExit()

    def get_post_comments(self, post_id: int, owner_id: int) -> dict:
        try:
            return self._session.wall.getComments(
                post_id=post_id, owner_id=owner_id)
        except VkAPIError:
            self._logger.vk_api_request_error()
            raise SystemExit()
