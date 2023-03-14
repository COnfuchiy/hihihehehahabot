import logging
import os

import numpy as np
import tensorflow as tf
from dependency_injector.wiring import inject, Provide
from keras.saving.legacy.save import load_model
from keras.utils import img_to_array

from src.image.entity import ImageObject
from src.nn.types import ImageTypes
from src.utils.logger import GeneralLogger

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

tf.get_logger().setLevel(logging.ERROR)
tf.autograph.set_verbosity(1)
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


class ImagePredictor:

    @inject
    def __init__(self,
                 logger: GeneralLogger = Provide['logger'],
                 path_to_model: str = Provide['config.path_to_model']):
        self._logger = logger
        self._path_to_model = path_to_model
        self._model = self._load_model()

    def _load_model(self):
        try:
            return load_model(
                os.path.dirname(__file__) +
                '/' +
                self._path_to_model)
        except (ImportError, IOError):
            self._logger.model_load_error(self._path_to_model)
            raise SystemExit()

    def predict(self, image_object: ImageObject) -> ImageTypes:
        image_as_array = img_to_array(image_object.image_to_predict())
        image_as_array = np.array([image_as_array])
        image_as_array = image_as_array / 255.0
        image_as_array = image_as_array.reshape(1, 128, 128, 3)
        pred = self._model.predict(image_as_array)
        if pred[0] > 0.5:
            return ImageTypes.MEM
        else:
            return ImageTypes.CAT
