from wordcloud import WordCloud
import jieba
from imageio import imread


def Cloud():
    # 数据来源
    filename = "data_file\\beijing1211_clean_utf8.csv"
    # 背景图片
    background = "resources\\background.jpg"
    # 储存地址
    savepath = "picture\\北京二手房数据词云.png"
    # 字体路径
    fontpath = "resources\\simhei.ttf"
    # 屏蔽词汇
    stopwords = ["null", "暂无", "数据", "上传", "照片", "房本", "供暖", "抵押"]

    # 读入数据文件
    comment_text = open(filename, encoding="utf-8").read()
    # 读取背景图片
    color_mask = imread(background)

    # 结巴分词,同时剔除掉不需要的词汇
    words = jieba.cut(comment_text)
    words = [word for word in words if word not in stopwords]
    cut_text = " ".join(words)

    # 设置词云格式
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path=fontpath,
        # 设置背景色
        background_color='white',
        # 词云形状
        mask=color_mask,
        # 允许最大词汇
        max_words=2000,
        # 最大号字体
        max_font_size=60
    )
    # 产生词云
    word_cloud = cloud.generate(cut_text)
    # 保存图片
    word_cloud.to_file(savepath)


# 程序入口
if __name__ == "__main__":
    Cloud()
