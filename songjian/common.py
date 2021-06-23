import pandas as pd
keys=["宋健","杨培谦","张道新","郝","赵继懋","李钧","李军","丰琅",
      "郭宇文","陈永骞","王文营","王金铭","吉正国","肖荆",
      "陈思阳","张峰波","朱熹","陈永骞","尚东浩","张磊","王磊","朱一辰"]
default_one = {}
for i in keys:
    default_one[i] = 0
default_one["其他"] = 0
default_one["其他医生"] = ""
default_one["全部"] = 0

def init(header):
    for i in keys:
        header.append(i)
        header.append("")
    header.extend(["其他", "", "其他医生", "全部"])

def check(two,doctor):
    inkeys = False
    for i in keys:
        if doctor.find(i) == 0:
            two[i] = two[i] + 1
            inkeys = True
            break
    if not inkeys:
        two["其他"] = two["其他"] + 1
        two["其他医生"] = two["其他医生"] + "，" + doctor
    two["全部"] = two["全部"] + 1

def compositeResults(results,header,filename):
    data = []

    # 组织二维数组
    for one in results:
        row = [one]
        # print(one,results[one])
        for key in keys:
            row.append(results[one][key])
            row.append("{:.2%}".format(results[one][key] / results[one]["全部"]))
        row.append(results[one]["其他"])
        row.append("{:.2%}".format(results[one]["其他"] / results[one]["全部"]))
        row.append(results[one]["其他医生"][1:])
        row.append(results[one]["全部"])
        data.append(row)
    save = pd.DataFrame(data)
    save.reset_index()
    save.columns = header

    # 排序
    save = save.sort_values(by="宋健", ascending=False)

    # 保存
    try:
        save.to_excel(filename, index=False)
    except:
        pass