from dataclasses import dataclass
from io import BytesIO

from PIL.Image import Image


@dataclass
class ImageObject:
    image: Image
    hash: str
    is_saved: bool = False

    def image_to_bytes(self) -> bytes:
        img_byte_array = BytesIO()
        try:
            self.image.save(img_byte_array, format='PNG')
        except ValueError:
            pass
        return img_byte_array.getvalue()

    def image_to_predict(self):
        return self.image.resize((128, 128))
