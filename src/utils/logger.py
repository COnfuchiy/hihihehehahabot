import logging
import os

from dependency_injector.wiring import Provide, inject


class GeneralLogger:
    _logger_name = 'app'
    _logger_level = logging.WARNING
    _logger_format = '%(asctime)s %(levelname)s %(message)s'

    @inject
    def __init__(
            self,
            log_filename: str = Provide['config.log_filename'],
            log_file_max_size_bytes: int = Provide['config.log_file_max_size_bytes']):
        self._log_filename = log_filename
        self._log_file_max_size_bytes = log_file_max_size_bytes
        self._logger = self._setup_logger_instance()

    def _warning(self, message: str):
        self._check_log_size()
        self._logger.warning(message)

    def _error(self, message: str, trace: bool = True):
        self._check_log_size()
        self._logger.error(message, exc_info=trace)

    def _check_log_size(self):
        log_file_size = os.path.getsize(self._log_filename)
        if log_file_size > self._log_file_max_size_bytes:
            open(self._log_filename, 'w').close()

    def _setup_logger_instance(self) -> logging.Logger:
        logger = logging.getLogger(self._logger_name)
        handler = logging.FileHandler(self._log_filename)
        formatter = logging.Formatter(self._logger_format)
        handler.setFormatter(formatter)
        handler.setLevel(self._logger_level)
        logger.addHandler(handler)
        return logger

    def vk_api_setup_error(self):
        self._error('VK API setup error')

    def vk_api_request_error(self):
        self._error('VK API request error')

    def image_request_error(self):
        self._error('VK image request error')

    def file_create_error(self, path):
        self._error(f'unable to create file {path}')

    def invalid_hashes_object(self):
        self._error('incorrect object format in file with image hashes', False)

    def max_iteration_post_search_reached(self):
        self._error(
            'maximum number of iterations for post search has been reached',
            False)

    def max_iteration_image_search_reached(self):
        self._error(
            'maximum number of iterations for image search has been reached',
            False)

    def model_load_error(self, path):
        self._error(f'error loading model from {path}')

    def telegram_setup_error(self):
        self._error('telegram bot setup error')

    def telegram_request_error(self):
        self._error('telegram bot request error')

    def telegram_image_converting(self):
        self._error('telegram json data converting')
