from dataclasses import dataclass


@dataclass(frozen=True)
class AttachmentDto:
    type: str
    url: str

    @staticmethod
    def from_dict(data: dict):
        attachment_type = data.get('type')
        if attachment_type not in data:
            attachment_url = ''
        else:
            attachment_url = data[attachment_type].get('url', '')
            if not attachment_url and 'sizes' in data[attachment_type]:
                attachment_url = AttachmentDto.get_max_size_attachment_url(
                    data[attachment_type]['sizes'])
        return AttachmentDto(
            type=attachment_type,
            url=attachment_url
        )

    @staticmethod
    def get_max_size_attachment_url(image_sizes) -> str:
        max_height = 0
        max_size_attachment_url = ''
        for size in image_sizes:
            current_height = size.get('height', 0)
            if current_height > max_height:
                max_height = current_height
                max_size_attachment_url = size.get('url', '')
        return max_size_attachment_url
