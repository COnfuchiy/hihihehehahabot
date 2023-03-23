from dataclasses import dataclass


@dataclass()
class Post:
    id: int
    is_donate: bool
    group_name: str
    marked_as_ads: bool
    attachments: list
    date: int
    likes: int
    owner_id: int
    text: str
    comments: list
