'''
article.py

CREATED:   22.01.2021 1:19
EDITED:    22.01.2021 1:19
PROJECT:   fama_models
AUTHOR:    Noah Kamara (developer@noahkamara.com)
LICENSE:   Mozilla Public License 2.0
COPYRIGHT: Noah Kamara
'''


from pydantic import BaseModel, AnyUrl
from typing import Optional, List



class Article(BaseModel):
    """ Model for Article """
    title: str
    short_title: str
    content: str
