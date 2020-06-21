# -*- coding:utf-8 -*-
import csv


def clean():
    # 数据读入
    filename = "data_file\\beijing1211_origin_utf8.csv"
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        context = [line for line in reader]

    # 数据写入
    with open("data_file\\beijing1211_clean_utf_test.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        # 逐条读取记录
        for line in context:
            # 去除每个数据项的空白符和换行符
            line = [x.strip() for x in line]
            if line[0] == "id":
                writer.writerow(line)
                continue

            # 对于一些未对齐的数据进行处理，主要是别墅、商业办公类建筑类型
            if "别墅" in line:
                line_copy = line[:]
                line[8] = "null"
                line[9] = line_copy[8]
                line[10] = "null"
                line[11] = line_copy[9]
                line[12] = line_copy[10]
                line[13] = line_copy[11]
                line[14] = "null"
                line[15] = line_copy[13]
                line[16] = "null"
                line[17] = line_copy[14]
                line[18] = line_copy[17]
                line[19] = line_copy[18]
                line[20] = line_copy[19]
                line[21] = line_copy[20]
                line[22] = line_copy[21]
                line[23] = line_copy[22]
                line[24] = line_copy[23]
                line.append(1)
                line[25] = line_copy[24]

            if "商业办公类" in line:
                while line[21] != "商业办公类":
                    del line[18]

            try:
                # 将总价数据项统一整理为整数
                float_num = float(line[3])
                line[3] = str(int(float_num))

                # 去除单价数据项单位
                line[4] = line[4].split("元")[0]

                # 去除建筑面积数据项的单位
                if line[7] != "null" and line[7] != "暂无数据":
                    line[7] = line[7].split("㎡")[0]

                # 去除套内面积数据项的单位
                if line[9] != "null" and line[9] != "暂无数据":
                    line[9] = line[9].split("㎡")[0]

                writer.writerow(line)
            except Exception as e:
                print("部分格式无法转换")


# 程序入口
if __name__ == "__main__":
    clean()
