from dataclasses import dataclass

from src.vk.domain.enum.attachment_types_enum import AttachmentTypes


@dataclass(frozen=True)
class Attachment:
    type: AttachmentTypes
    url: str
