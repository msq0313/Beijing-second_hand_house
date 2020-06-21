import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 北京二手房房屋用途水平柱状图
# 北京二手房房屋户型占比图
# 北京二手房建筑类型占比图
# 北京二手房房源朝向分布图
# 北京二手房建筑面积分布图
# 北京二手房装修情况占比图
def house_output():
    # 数据加载
    # 定义加载数据的文件名
    filename = "data_file\\beijing1211_clean_utf8.csv"
    # 自定义数据的行列索引
    names = [
        "id", "communityName", "areaName", "total", "unitPriceValue",
        "fwhx", "szlc", "jzmj", "hxjg", "tnmj",
        "jzlx", "fwcx", "jzjg", "zxqk", "thbl", "gnfs",
        "pbdt", "cqnx", "gpsj", "jyqs", "scjy",
        "fwyt", "fwnx", "cqss", "dyxx", "fbbj",
    ]
    # 自定义缺失值标记列表
    miss_value = ["null", "暂无数据"]
    # 使用自定义的列名，跳过文件中的头行，处理缺失值列表标记的缺失值
    df = pd.read_csv(filename, skiprows=[0], names=names, na_values=miss_value)
    print(df.info())

    # 北京二手房房屋用途水平柱状图
    count_fwyt = df["fwyt"].value_counts(ascending=True)
    count_fwyt.name = ""
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_xlabel("房源数量(套)", fontsize=14)
    ax.set_title("北京二手房房屋用途水平柱状图", fontsize=18)
    count_fwyt.plot(kind="barh", fontsize=12, grid=True)
    plt.savefig("picture\\北京二手房房屋用途占水平柱状图.png")
    # plt.show()

    # 北京二手房房屋户型占比图
    count_fwhx = df['fwhx'].value_counts()[:10]
    # 超过十种以上，统一归类为其他
    count_other_fwhx = pd.Series({"其他": df['fwhx'].value_counts()[10:].count()})
    count_fwhx = count_fwhx.append(count_other_fwhx)
    count_fwhx.index.name = ""
    count_fwhx.name = ""
    fig = plt.figure(figsize=(9, 9))
    # 将画布分割成1行1列，图像画在从左到右从上到下的第1块
    ax = fig.add_subplot()
    ax.set_title("北京二手房房屋户型占比图", fontsize=18)
    count_fwhx.plot(kind="pie", cmap=plt.cm.plasma, autopct="%3.1f%%", fontsize=12, grid=True)
    plt.legend(loc="upper right", fontsize=14, bbox_to_anchor=(1.1, 1.05))
    plt.savefig("picture\\北京二手房房屋户型占比图.png")
    # plt.show()

    # 北京二手房建筑类型占比图
    count_jzlx = df["jzlx"].value_counts()
    count_jzlx.name = ""
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot()
    ax.set_title("北京二手房建筑类型占比图", fontsize=18)
    count_jzlx.plot(kind="pie", cmap=plt.cm.plasma, autopct="%3.1f%%", fontsize=12, grid=True)
    plt.legend(loc="upper right", fontsize=14, bbox_to_anchor=(1.1, 1.05))
    plt.savefig("picture\\北京二手房建筑类型占比图.png")
    # plt.show()

    # 北京二手房房源朝向分布图
    count_fwcx = df["fwcx"].value_counts()[:15]
    count_other_fwcx = pd.Series({"其他": df['fwcx'].value_counts()[15:].count()})
    count_fwcx = count_fwcx.append(count_other_fwcx)
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_title("房源朝向分布情况", fontsize=18)
    count_fwcx.plot(kind="bar", fontsize=12, grid=True)
    plt.savefig("picture\\北京二手房房屋朝向分布情况.png")
    # plt.show()

    # 北京二手房建筑面积分布图
    area_level = [0, 50, 100, 150, 200, 250, 300, 500]
    label_level = ['小于50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350']
    jzmj_cut = pd.cut(df["jzmj"], area_level, labels=label_level)
    jzmj_result = jzmj_cut.value_counts()
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_ylabel("建筑面积(㎡)", fontsize=14)
    ax.set_title("北京二手房建筑面积分布图", fontsize=18)
    jzmj_result.plot(kind="barh", fontsize=12, grid=True)
    plt.savefig("picture\\北京二手房建筑面积分布区间.png")
    # plt.show()

    # 北京二手房装修情况占比图
    count_zxqk = df["zxqk"].value_counts()
    count_zxqk.name = ""
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot()
    ax.set_title("北京二手房装修情况占比图", fontsize=18)
    count_zxqk.plot(kind="pie", cmap=plt.cm.plasma, autopct="%3.1f%%", fontsize=12, grid=True)
    plt.legend(loc="upper right", fontsize=14, bbox_to_anchor=(1.1, 1.05))
    plt.savefig("picture\\北京二手房装修情况占比图.png")
    # plt.show()


# 程序入口
if __name__ == "__main__":
    house_output()
