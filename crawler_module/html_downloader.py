import requests
from crawler_module.log_module import Log
import random


# 网页下载
class HtmlDownloader:

    # 初始化
    def __init__(self):
        self.log = Log("html_downloader", "logs")
        self.user_agent = [
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE) ",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0) ",
            "Mozilla/5.0 (Windows NT 5.1; zh-CN; rv:1.9.1.3) Gecko/20100101 Firefox/8.0",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        ]

    def download(self, url):
        if url is None:
            self.log.logger.error("页面下载：url为空!!!")
            return None

        # 随机变换user-agent
        # 请求头
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Host": "bj.lianjia.com",
            # "Host":"sh.lianjia.com",
            "User-Agent": random.choice(self.user_agent)
        }

        # get请求
        r = requests.get(url, headers=headers)

        if r.status_code != 200:
            self.log.logger.error("页面下载：响应错误：%d" % r.status_code)
            return None

        self.log.logger.info("页面下载：成功!")
        print("页面下载：成功!")
        return r.text
