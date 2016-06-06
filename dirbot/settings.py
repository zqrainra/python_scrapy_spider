# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Content'

# ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
ITEM_PIPELINES = {'dirbot.pipelines.StoreInMysql': 1}
IMAGES_STORE = 'downloads/imgs'
IMAGES_URLS_FIELD = 'image_urls'
IMAGES_RESULT_FIELD = 'images'
BOT_NAME = 'dmoz'
#
# SPIDER_MODULES = ['dirbot.spiders']
# NEWSPIDER_MODULE = 'dirbot.spiders'