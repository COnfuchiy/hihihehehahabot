from dataclasses import dataclass


@dataclass
class Comment:
    id: int
    text: str
    attachments: list
