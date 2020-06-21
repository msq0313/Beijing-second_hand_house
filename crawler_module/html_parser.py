from bs4 import BeautifulSoup
from crawler_module.log_module import Log


# 网页解析
# 使用BeautifulSoup库
class HtmlParser:

    def __init__(self):
        self.log = Log("html_parser", "logs")

    def get_urls(self, html_cont):
        # 获取二手房页面的链接
        if html_cont is None:
            self.log.logger.error("页面解析(page)：pg页面为空！")
            print("页面解析(page)：pg页面为空！")
            return

        urls = set()
        bsObj = BeautifulSoup(html_cont, "html.parser")

        sellListContent = bsObj.find("ul", {"class": "sellListContent"})

        if sellListContent is not None:
            for child in sellListContent.children:
                if child["class"][0] == "clear":
                    urls.add(child.a["href"])
                    self.log.logger.info(child.a["href"])
                    # print(child.find("a",{"class":"img"})["href"])
        else:
            self.log.logger.error("页面解析(page)：找不到sellListContent标签！")

        self.log.logger.info("PG页面解析：pg页面解析成功！")
        print("页面解析：pg页面解析成功！")
        return urls

    def get_data(self, html_cont, id):
        # 获取二手房页面详细数据
        if html_cont is None:
            self.log.logger.error("页面解析(detail)：传入页面为空！")
            print("页面解析(detail)：传入页面为空！")
            return

        data = []
        communityName = "null"
        areaName = "null"
        total = "null"
        unitPriceValue = "null"

        bsObj = BeautifulSoup(html_cont, "html.parser")

        tag_com = bsObj.find("div", {"class": "communityName"}).find("a")
        if tag_com is not None:
            communityName = tag_com.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到communityName标签！")

        tag_area = bsObj.find("div", {"class": "areaName"}).find("span", {"class": "info"}).find("a")
        if tag_area is not None:
            areaName = tag_area.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到areaName标签！")

        tag_total = bsObj.find("span", {"class": "total"})
        if tag_total is not None:
            total = tag_total.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到total标签！")

        tag_unit = bsObj.find("span", {"class": "unitPriceValue"})
        if tag_unit is not None:
            unitPriceValue = tag_unit.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到total标签！")

        data.append(id)
        data.append(communityName)
        data.append(areaName)
        data.append(total)
        data.append(unitPriceValue)

        counta = 12
        for a_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "base"}).find("div", {
            "class": "content"}).ul.findAll("li"):
            # print(child1)
            [s.extract() for s in a_child("span")]
            data.append(a_child.get_text())
            counta = counta - 1

        while counta > 0:
            data.append("null")
            counta = counta - 1

        countb = 8
        for b_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "transaction"}).find("div", {
            "class": "content"}).ul.findAll("li"):
            information = b_child.span.next_sibling.next_sibling.get_text()
            data.append(information)
            countb = countb - 1

        while countb > 0:
            data.append("null")
            countb = countb - 1

        self.log.logger.info("页面解析(detail)：页面解析成功！")
        print("页面解析(detail)：页面解析成功！")
        return data


