import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 北京各区域二手房平均单价图
# 北京各区域二手房单价箱线图
# 北京各区域二手房总价箱线图
# 北京各区域二手房平均建筑面积
# 北京二手房单价最高小区排名
# 北京二手房总价与建筑面积散点图
# 北京二手房单价与建筑面积散点图
def price_output():
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
    # print(df.info())

    # 北京各区域二手房平均单价图
    groups_unitprice_area = df["unitPriceValue"].groupby(df["areaName"])
    mean_unitprice = groups_unitprice_area.mean()
    mean_unitprice.index.name = ""
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_ylabel("单价(元/平米)", fontsize=14)
    ax.set_title("北京各区域二手房平均单价图", fontsize=18)
    mean_unitprice.plot(kind="bar", fontsize=12, grid=True)
    plt.savefig("picture\\北京各区域二手房平均单价图.png")
    # plt.show()

    # 北京各区域二手房单价箱线图
    box_unitprice_area = df["unitPriceValue"].groupby(df["areaName"])
    box_data = pd.DataFrame(list(range(12000)), columns=["start"])
    for name, group in box_unitprice_area:
        box_data[name] = group
    del box_data["start"]
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_ylabel("总价(万元)", fontsize=14)
    ax.set_title("北京各区域二手房单价箱线图", fontsize=18)
    box_data.plot(kind="box", fontsize=12, sym='go', grid=True, ax=ax,
                  yticks=[20000, 60000, 100000, 140000, 200000])
    plt.savefig("picture\\北京各区域二手房单价箱线图.png")
    # plt.show()

    # 北京各区域二手房总价箱线图
    box_total_area = df["total"].groupby(df["areaName"])
    flag = True
    box_data = pd.DataFrame(list(range(12000)), columns=["start"])
    for name, group in box_total_area:
        box_data[name] = group
    del box_data["start"]
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_ylabel("总价(万元)", fontsize=14)
    ax.set_title("北京各区域二手房总价箱线图", fontsize=18)
    box_data.plot(kind="box", fontsize=12, sym="go", grid=True, ax=ax,
                  yticks=[0, 1000, 2000, 3000, 4000, 5000, 7000])
    plt.savefig("picture\\北京各区域二手房总价箱线图1.png")
    box_data.plot(kind="box", fontsize=12, sym="go", grid=True, ax=ax,
                  yticks=[0, 250, 500, 1000, 1500, 2000, 3000], ylim=[0, 3000])
    plt.savefig("picture\\北京各区域二手房总价箱线图2.png")
    # plt.show()

    # 北京各区域二手房平均建筑面积
    groups_area_jzmj = df["jzmj"].groupby(df["areaName"])
    mean_jzmj = groups_area_jzmj.mean()
    mean_jzmj.index.name = ""
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_ylabel("建筑面积(㎡)", fontsize=14)
    ax.set_title("北京各区域二手房平均建筑面积", fontsize=18)
    mean_jzmj.plot(kind="bar", fontsize=12, grid=True)
    plt.savefig("picture\\北京各区域二手房平均建筑面积.png")
    # plt.show()

    # 北京二手房单价最高小区排名
    unitprice_top = df.sort_values(by="unitPriceValue", ascending=False)[:10]
    unitprice_top = unitprice_top.sort_values(by="unitPriceValue")
    unitprice_top.set_index(unitprice_top["communityName"], inplace=True)
    unitprice_top.index.name = ""
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_ylabel("单价(元/平米)", fontsize=14)
    ax.set_title("北京二手房单价最高小区排名", fontsize=18)
    unitprice_top["unitPriceValue"].plot(kind="barh", fontsize=12, grid=True)
    plt.savefig("picture\\北京二手房单价最高小区排名.png")
    # plt.show()

    # 北京二手房总价与建筑面积散点图
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_title("北京二手房总价与建筑面积散点图", fontsize=18)
    df.plot(x="jzmj", y="total", kind="scatter", grid=True, fontsize=12, ax=ax, alpha=0.4,
            xticks=[0, 50, 100, 150, 200, 250, 300, 400, 500, 600], xlim=[0, 700])
    ax.set_xlabel("建筑面积(㎡)", fontsize=14)
    ax.set_ylabel("总价(万元)", fontsize=14)
    plt.savefig("picture\\北京二手房总价与建筑面积散点图.png")
    # plt.show()

    # 北京二手房单价与建筑面积散点图
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot()
    ax.set_title("北京二手房单价与建筑面积散点图", fontsize=18)
    df.plot(x="jzmj", y="unitPriceValue", kind="scatter", grid=True, fontsize=12, ax=ax, alpha=0.4,
            xticks=[0, 50, 100, 150, 200, 250, 300, 400, 500, 600], xlim=[0, 700])
    ax.set_xlabel("建筑面积(㎡)", fontsize=14)
    ax.set_ylabel("单价(元/平米)", fontsize=14)
    plt.savefig("picture\\北京二手房单价与建筑面积散点图.png")
    # plt.show()


# 程序入口
if __name__ == "__main__":
    price_output()
