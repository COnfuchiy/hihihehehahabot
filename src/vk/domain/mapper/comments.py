from src.vk.domain.dto.comments import CommentDto, CommentsDto
from src.vk.domain.entity.comment import Comment
from src.vk.domain.mapper.has_attachments import HasAttachmentsMapper


class CommentMapper(HasAttachmentsMapper):

    @staticmethod
    def to_entity(comment_dto: CommentDto) -> Comment:
        attachments: list = CommentMapper.get_attachments_entities(
            comment_dto.attachments)
        if len(attachments):
            return Comment(
                id=comment_dto.id,
                text=comment_dto.text,
                attachments=attachments
            )
        return None


class CommentsMapper:
    @staticmethod
    def from_dto(comments_dto: CommentsDto) -> list:
        comments: list = []
        for comment_dto in comments_dto.comments:
            comment_entity: Comment = CommentMapper.to_entity(
                comment_dto)
            if comment_entity:
                comments.append(comment_entity)
        return comments
