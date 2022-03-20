# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ActivitiesItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()
    P_name = scrapy.Field()
    P_rank = scrapy.Field()
    P_type = scrapy.Field()
    P_status = scrapy.Field()
    P_time = scrapy.Field()
    P_images = scrapy.Field()
    P_url = scrapy.Field()
    P_rate = scrapy.Field()
    Total_reviewers = scrapy.Field()
    R_5points = scrapy.Field()
    R_4points = scrapy.Field()
    R_3points = scrapy.Field()
    R_2points = scrapy.Field()
    R_1points = scrapy.Field()
    R_name = scrapy.Field()
    R_address = scrapy.Field()
    R_idea = scrapy.Field()
    R_content = scrapy.Field()
    Time_who = scrapy.Field()
    R_time = scrapy.Field()
    pass 
