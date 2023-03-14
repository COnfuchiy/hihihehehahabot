from src.vk.domain.dto.attachment import AttachmentDto
from src.vk.domain.entity.attachment import Attachment
from src.vk.domain.enum.attachment_types_enum import AttachmentTypes


class AttachmentMapper:

    @staticmethod
    def to_entity(attachment_dto: AttachmentDto) -> Attachment:
        attachment_type = AttachmentMapper._get_type_from_str(
            attachment_dto.type)
        if attachment_type and attachment_dto.url:
            return Attachment(
                type=attachment_type,
                url=attachment_dto.url
            )
        return None

    @staticmethod
    def _get_type_from_str(attachment_type: str) -> AttachmentTypes:
        if attachment_type == AttachmentTypes.TYPE_IMAGE.value:
            return AttachmentTypes.TYPE_IMAGE
        else:
            return None
