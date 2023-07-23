# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    platform = scrapy.Field()       # 平台
    likes = scrapy.Field()         # 点赞
    comments = scrapy.Field()          # 评论
    favorites = scrapy.Field()       # 收藏
    shares = scrapy.Field()          # 转发
    username = scrapy.Field()           # 用户名
    user_id = scrapy.Field()            # 用户id
    video_title = scrapy.Field()          # 视频标题
    video_play_link = scrapy.Field()            # 视频播放链接
    publish_time = scrapy.Field()           # 发布时间
    tags = scrapy.Field()           # tag标签
    author_head = scrapy.Field()    # 作者头像
