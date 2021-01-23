'''
rss_feed.py

CREATED:   22.01.2021 1:19
EDITED:    22.01.2021 1:19
PROJECT:   fama_models
AUTHOR:    Noah Kamara (developer@noahkamara.com)
LICENSE:   Mozilla Public License 2.0
COPYRIGHT: Noah Kamara
'''


from pydantic import BaseModel, AnyUrl, validator
from typing import Optional
from .data import Data

LANGUAGES = Data.load("languages.json")


class RSSFeed(BaseModel):
    """ Model for RSS-Feed """
    title: str
    subtitle: Optional[str] = None
    language: Optional[str] = None
    link: AnyUrl
    description: Optional[str] = None
    image: Optional[AnyUrl] = None

    @validator('language')
    def language_is_valid_code(cls, v):
        if v is None:
            return None

        v = v.lower()

        if v not in LANGUAGES:
            return None

        return LANGUAGES[v].upper()
