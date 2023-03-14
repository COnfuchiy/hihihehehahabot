from dataclasses import dataclass

from src.vk.domain.dto.attachment import AttachmentDto


@dataclass(frozen=True)
class PostDto:
    id: int
    is_donate: bool
    marked_as_ads: bool
    attachments: list
    date: int
    likes: int
    owner_id: int
    text: str

    @staticmethod
    def from_dict(data: dict):
        post_id: int = data.get('id', 0)
        is_donate: bool = data['donut'].get(
            'is_donut', False) if 'donut' in data else False
        marked_as_ads: bool = data.get('marked_as_ads', False)
        post_attachments = []
        for attachment in data.get('attachments', []):
            post_attachments.append(
                AttachmentDto.from_dict(attachment)
            )
        date: int = data.get('date', 0)
        likes: int = data['likes'].get(
            'count', 0) if 'likes' in data else 0
        owner_id = data.get('owner_id', 0)
        text = data.get('text', '')
        return PostDto(
            id=post_id,
            is_donate=is_donate,
            marked_as_ads=marked_as_ads,
            attachments=post_attachments,
            date=date,
            likes=likes,
            owner_id=owner_id,
            text=text
        )
