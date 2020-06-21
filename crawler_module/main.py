from crawler_module.url_manager import UrlManager
from crawler_module.log_module import Log
from crawler_module.html_downloader import HtmlDownloader
from crawler_module.html_parser import HtmlParser
from crawler_module.html_outputter import OutPutter
import time
import random


class Main:

    def __init__(self):
        self.urls = UrlManager()
        self.log = Log("spider_main", "logs")
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputter = OutPutter()

    def craw(self, root_url):
        # 地点设置
        global detail_url
        # areas1为北京，areas2为上海
        areas1 = {
            "dongcheng", "xicheng", "chaoyang", "haidian",
            "fengtai", "shijingshan", "tongzhou", "changping",
            "daxing", "shunyi", "fangshan", "mentougou",
            "pinggu", "huairou", "miyun", "yanqing",
        }

        areas2 = {
            "pudong", "minhang", "baoshan", "xuhui",
            "putuo", "yangpu", "changning", "songjiang",
            "jiading", "huangpu", "jingan", "hongkou",
            "qingpu", "fengxian", "jinshan",
        }

        # 1、从二手房列表网页抓取详情界面链接，并将连接放入URL管理模块
        pg = 2
        # pg为指定页数
        for area in areas1:
            for num in range(1, pg):
                pg_url = root_url + area + "/pg" + str(num) + "/"
                # 拼接页面地址: https://bj.lianjia.com/ershoufang/pg2  北京
                self.log.logger.info("拼接页面地址：" + pg_url)
                print("拼接页面地址：" + pg_url)
                # 启动下载器,下载页面
                try:
                    html_cont = self.downloader.download(pg_url)
                except Exception as e:
                    self.log.logger.error("下载页面出现异常:" + repr(e))
                    time.sleep(60 * 30)
                else:
                    # 解析PG页面，获得二手房详情页面的链接,并将所有链接放入URL管理模块
                    try:
                        urls = self.parser.get_urls(html_cont)
                    except Exception as e:
                        self.log.logger.error("页面解析出现异常:" + repr(e))
                    else:
                        self.urls.add_new_urls(urls)
                        # 暂停0~3秒的整数秒，时间区间：[0,3]
                        time.sleep(random.randint(0, 3))

        # time.sleep(60 * 20)
        # 2、解析二手房具体页面
        recordID = 1
        stop = 1
        while self.urls.has_new_url():
            # 获取url
            try:
                detail_url = self.urls.get_new_url()
                self.log.logger.info("二手房页面地址：" + detail_url)
                print("二手房页面地址：" + detail_url)
            except Exception as e:
                print("拼接地址出现异常")
                self.log.logger.error("拼接地址出现异常:" + detail_url)

            # 下载页面
            try:
                detail_html = self.downloader.download(detail_url)
            except Exception as e:
                self.log.logger.error("下载页面出现异常:" + repr(e))
                self.urls.add_new_url(detail_url)
                time.sleep(60 * 30)
            else:
                # 解析页面
                try:
                    data = self.parser.get_data(detail_html, recordID)
                except Exception as e:
                    self.log.logger.error("解析页面出现异常:" + repr(e))
                else:
                    # 输出数据
                    try:
                        self.outputter.collect_data(data)
                    except Exception as e:
                        self.log.logger.error("输出数据出现异常:" + repr(e))
                    else:
                        print('第', recordID, "条记录")
                        recordID = recordID + 1
                        stop = stop + 1
                        # 暂停0~3秒的整数秒，时间区间：[0,3]
                        time.sleep(random.randint(0, 3))
                        if stop == 2500:
                            stop = 1
                            time.sleep(60 * 20)


# 程序入口
if __name__ == "__main__":
    # 设定爬虫入口URL
    # 除北京外曾尝试爬取上海二手房信息
    root_url = "https://bj.lianjia.com/ershoufang/"
    # root_url = "https://sh.lianjia.com/ershoufang/"

    # 启动爬虫
    Main().craw(root_url)
