```python
import os
from scrapy.exceptions import DropItem

class MyanimelistPipeline(object):
    def __init__(self):
        self.file = open('character_traits.txt', 'w')

    def process_item(self, item, spider):
        if item['character_traits']:
            line = f"{item['character_name']}: {', '.join(item['character_traits'])}\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing character_traits in %s" % item)

    def close_spider(self, spider):
        self.file.close()
```