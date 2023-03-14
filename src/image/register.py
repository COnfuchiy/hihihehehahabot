import os.path

import joblib
from dependency_injector.wiring import inject, Provide

from src.image.entity import ImageObject
from src.utils.logger import GeneralLogger


class ImageRegister:

    @inject
    def __init__(
            self,
            logger: GeneralLogger = Provide['logger'],
            image_hashes_filename: str = Provide['config.image_hashes_filename'],
            max_stored_hashes: int = Provide['config.max_stored_hashes']):
        self._logger = logger
        self._image_hashes_filename = image_hashes_filename
        self._max_stored_hashes = max_stored_hashes
        self._hashes = self._get_all_hashes()

    def check_image_hash_existing(self, image_object: ImageObject):
        return True if image_object.hash in self._hashes else False

    def _get_all_hashes(self) -> list:
        if not os.path.exists(self._image_hashes_filename):
            self._create_storage()
        hashes = joblib.load(self._image_hashes_filename)
        if not isinstance(hashes, list):
            self._logger.invalid_hashes_object()
            return []
        if len(hashes) > self._max_stored_hashes:
            return []
        return hashes

    def _create_storage(self):
        try:
            joblib.dump([], self._image_hashes_filename)
        except OSError:
            self._logger.file_create_error(self._image_hashes_filename)
            raise SystemExit

    def add_hash(self, image_object: ImageObject):
        self._hashes.append(image_object.hash)
        self._save_hashes()

    def _save_hashes(self):
        try:
            joblib.dump(self._hashes, self._image_hashes_filename)
        except OSError:
            self._logger.file_create_error(self._image_hashes_filename)
            raise SystemExit
