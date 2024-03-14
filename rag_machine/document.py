from typing import Optional
import uuid


class Document:
    def __init__(self,  content: str, title: Optional[str] = None, canonical_url: Optional[str] = None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.canonical_url = canonical_url
