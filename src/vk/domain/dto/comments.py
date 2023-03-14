from dataclasses import dataclass

from src.vk.domain.dto.attachment import AttachmentDto


@dataclass(frozen=True)
class CommentDto:
    id: int
    text: str
    attachments: list


@dataclass()
class CommentsDto:
    comments: list

    @staticmethod
    def from_dict(data: dict):
        comments = []
        for comment in data.get('items', []):
            comment_id = comment.get('id')
            comment_text = comment.get('text')
            comment_attachments = []
            for attachment in comment.get('attachments', []):
                comment_attachments.append(
                    AttachmentDto.from_dict(attachment)
                )
            comments.append(
                CommentDto(
                    id=comment_id,
                    text=comment_text,
                    attachments=comment_attachments
                )
            )
        return CommentsDto(
            comments=comments
        )
