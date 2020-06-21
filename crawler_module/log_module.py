import logging
import datetime


# 日志类
class Log:

    def __init__(self, name, filepath):
        # 初始化日志器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 生成相应日期的日志文件
        filepath = (filepath + "\\" + str(datetime.date.today()) + " log.txt")
        self.fh = logging.FileHandler(filepath)
        self.fh.setLevel(logging.DEBUG)

        # 初始化格式器
        self.formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
