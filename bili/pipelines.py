# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class BiliPipeline:
    def __init__(self, db_params):
        self.db_params = db_params

    @classmethod
    def from_crawler(cls, crawler):
        db_params = {'host': 'localhost', 'port': 3306, 'user': 'root',  # 用户名
            'password': '123456',  # 密码
            'database': 'videoswebdb',  # 统一数据库名
            'charset': 'utf8mb4', }
        return cls(db_params)

    def open_spider(self, spider):
        self.conn = pymysql.connect(**self.db_params)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        # 根据实际情况编写插入数据的SQL语句
        # 表名 video
        sql = """
            INSERT INTO video (platform, likes, comments, favorites,shares,username,user_id,video_title,video_play_link,publish_time,tags,author_head)
            VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
        item['platform'], item['likes'], item['comments'], item['favorites'], item['shares'], item['username'],
        item['user_id'], item['video_title'], item['video_play_link'], item['publish_time'], item['tags'],
        item['author_head'],)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return item
