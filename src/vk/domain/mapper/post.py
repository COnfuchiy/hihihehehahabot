from src.vk.domain.dto.comments import CommentsDto
from src.vk.domain.dto.post import PostDto
from src.vk.domain.entity.attachment import Attachment
from src.vk.domain.entity.comment import Comment
from src.vk.domain.entity.post import Post
from src.vk.domain.mapper.comments import CommentsMapper
from src.vk.domain.mapper.has_attachments import HasAttachmentsMapper


class PostMapper(HasAttachmentsMapper):

    @staticmethod
    def to_entity(
            post_dto: PostDto,
            group_name: str = '',
            comments_dto: CommentsDto = None) -> Post:
        attachments: list[Attachment] = PostMapper.get_attachments_entities(
            post_dto.attachments)
        if not len(attachments):
            return None
        if comments_dto:
            comments: list[Comment] = CommentsMapper.from_dto(comments_dto)
        else:
            comments = []
        return Post(
            id=post_dto.id,
            is_donate=post_dto.is_donate,
            group_name=group_name,
            marked_as_ads=post_dto.marked_as_ads,
            attachments=attachments,
            date=post_dto.date,
            likes=post_dto.likes,
            owner_id=post_dto.owner_id,
            text=post_dto.text,
            comments=comments
        )
