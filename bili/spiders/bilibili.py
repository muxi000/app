import scrapy
import re
from lxml import html
from scrapy import cmdline
from bili.items import BiliItem
import urllib.parse
class BilibiliSpider(scrapy.Spider):
    name = "bilibili"
    _list = []
    # allowed_domains = ["bilibili.com"]
    # start_urls = ["https://bilibili.com"]
    def start_requests(self):
        self.headers = {'authority': 'api.bilibili.com', 'accept': 'application/json, text/plain, */*',
                   'accept-language': 'zh-CN,zh;q=0.9',
                   'origin': 'https://www.bilibili.com', 'referer': 'https://www.bilibili.com/',
                   'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                   'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', }
        self.cookies = {'buvid3': 'f'}
        for i in range(10):
            url = 'https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?web_location=1430650&y_num=3&fresh_type=4&feed_version=V8&fresh_idx_1h=1&fetch_row=4&fresh_idx=1&brush=1&homepage_ver=1&ps=12&last_y_num=4&screen=862-793&outside_trigger=&last_showlist=av_n_487714434,av_n_785241113,av_n_997925107,av_n_615388235,av_272662535,av_742820613,av_n_357808888,av_n_870300935,av_n_615396070,av_n_955126160&uniq_id=909675189110&w_rid=04ebb1847ff8a91e78922a425352775c&wts=1688265372'
            yield scrapy.Request(url=url,headers=self.headers, cookies=self.cookies,callback=self.parse,dont_filter=True)

    def parse(self, response,**kwargs):
        res = response.json()
        for i in res['data']['item']:
            if i['bvid']:
                self._list.append(i['uri'])
                print(i['uri'])
                print(len(set(self._list)))
                yield scrapy.Request(url=i['uri'], headers=self.headers, cookies=self.cookies,callback=self.parse_index,
                    meta={'uri':i['uri']})
    def parse_index(self,response):
        video_info = BiliItem()
        try:
            res = response.text
            tree = html.fromstring(res)
        # 平台
            video_info['platform'] = 'bili'
        # 点赞
            video_info['likes'] = re.findall('"like":(.*?),', res)[0]
        # 评论
            video_info['comments'] = re.findall('"reply":(.*?),', res)[0]
        # 收藏
            video_info['favorites'] = re.findall('"favorite":(.*?),', res)[0]
        # 转发
            video_info['shares'] = re.findall('"share":(.*?),', res)[0]
        # 用户名
            video_info['username'] = re.findall('"owner.*?name":"(.*?)","face"', res)[0]
        # 用户id
            video_info['user_id'] = re.findall('"owner":\{"mid":(.*?),"name"', res)[0]
        # 视频标题
            video_info['video_title'] = re.findall('"title":"(.*?)","pubda', res)[0]
        # 视频播放链接
            video_info['video_play_link'] = response.meta['uri']
        # 发布时间
            video_info['publish_time'] = re.findall('datePublished" content="(.*?)"', res)[0]
        # tag标签
            tags = []
            tag_links = tree.xpath('//a[@class="tag-link"]/text()')
            for tag_link in tag_links:
                tags.append(tag_link)
            video_info['tags'] = tags
        # 作者头像
            video_info['author_head'] = urllib.parse.unquote(re.findall('"face":"(.*?)"},"s',res)[0].encode().decode('unicode_escape'))
            yield video_info
        except Exception as e:
            print(f'---------------------{response.meta["uri"]}---------{e}---------------------')  # 非短视频内容



cmdline.execute(["scrapy","crawl","bilibili"])

