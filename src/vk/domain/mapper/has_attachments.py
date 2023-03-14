from src.vk.domain.mapper.attachment import AttachmentMapper


class HasAttachmentsMapper:

    @staticmethod
    def get_attachments_entities(attachments_dto_list: list):
        attachments: list = []
        for attachment_dto in attachments_dto_list:
            attachment_entity = AttachmentMapper.to_entity(attachment_dto)
            if attachment_entity:
                attachments.append(attachment_entity)
        return attachments
