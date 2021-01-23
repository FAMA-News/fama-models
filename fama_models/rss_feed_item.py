'''
rss_feed_item.py

CREATED:   22.01.2021 1:19
EDITED:    22.01.2021 1:19
PROJECT:   fama_models
AUTHOR:    Noah Kamara (developer@noahkamara.com)
LICENSE:   Mozilla Public License 2.0
COPYRIGHT: Noah Kamara
'''


from pydantic import BaseModel, AnyUrl

class RSSFeedItem(BaseModel):
    """ Model for RSS-Feed-Model """
    title: str
    link: AnyUrl
    content: str
    image: AnyUrl