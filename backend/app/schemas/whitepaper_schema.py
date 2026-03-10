from pydantic import BaseModel
from typing import List, Optional

class WhitepaperResponse(BaseModel):
    id: str
    title: str
    slug: str
    description: str
    tags: Optional[List[str]]
    published_date: Optional[str]