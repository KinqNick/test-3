```python
import scrapy

class MyanimelistItem(scrapy.Item):
    # define the fields for your item here like:
    manga_title = scrapy.Field()
    character_name = scrapy.Field()
    character_traits = scrapy.Field()
```