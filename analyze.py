from pywebio.output import put_html
import csv
from pyecharts.charts import Bar, Pie
from pyecharts import options as opts


def handle():
    put_html(proportionBar)
    put_html(proportionPie())
    put_html(Proportion())
    put_html(incomeProfit())

@property
def proportionBar():
    nationDict = {}
    with open(r'Fortune500After.csv', encoding='utf-8') as jd:
        for i in range(1):
            jd.readline()  # 跳过第一行
        for row in csv.reader(jd):
            if row[4] not in nationDict:
                nationDict[row[4]] = 1
            else:
                nationDict[row[4]] += 1
    nationValueList = []
    nationKeyList = []
    for key in nationDict:
        nationValueList.append(nationDict[key])
        nationKeyList.append(key)
    bar = Bar()
    bar.add_xaxis(nationKeyList)
    bar.add_yaxis("世界500强数量", nationValueList)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="各个国家拥有世界500强企业"),
                        xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 45}))

    return bar


def proportionPie():
    nationDict = {}
    with open(r'Fortune500After.csv', encoding='utf-8') as jd:
        for i in range(1):
            jd.readline()  # 跳过第一行
        for row in csv.reader(jd):
            if row[4] not in nationDict:
                nationDict[row[4]] = 1
            else:
                nationDict[row[4]] += 1
    nationValueList = []
    nationKeyList = []
    for key in nationDict:
        nationValueList.append(nationDict[key])
        nationKeyList.append(key)
    pie = Pie()
    pie.add('数量', [list(z) for z in zip(nationKeyList, nationValueList)], radius='45%', center=["50%", "65%"])
    return pie


def incomeProfit():
    company = []
    income = []
    profit = []
    proportion = []
    with open(r'Fortune500After.csv', encoding='utf-8') as jd:
        for i in range(1):
            jd.readline()  # 跳过第一行
        for row in csv.reader(jd):
            try:
                if float(row[3]) > 0:
                    company.append(row[1])
                    income.append(float(row[2]))
                    profit.append(float(row[3]))
                    temp = float(row[3]) / float(row[2]) * 100
                    proportion.append(temp)
            except Exception:
                pass
    bar = Bar(init_opts=opts.InitOpts(width='4000px', height='30000px'))
    bar.add_xaxis(company)
    bar.add_yaxis("营业收入", income)
    bar.add_yaxis("利润", profit)
    # bar.add_yaxis("利润占营业收入", proportion)
    bar.reversal_axis()
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    bar.set_global_opts(title_opts=opts.TitleOpts(title="营业收入与利润（不包括利润小于0）"))
    return bar


def Proportion():
    company = []
    proportion = []
    with open(r'Fortune500After.csv', encoding='utf-8') as jd:
        for i in range(1):
            jd.readline()  # 跳过第一行
        for row in csv.reader(jd):
            try:
                if float(row[3]) > 0:
                    company.append(row[1])
                    temp = float(row[3]) / float(row[2]) * 100
                    proportion.append(temp)
            except Exception:
                pass
    bar = Bar(init_opts=opts.InitOpts(width='4000px', height='30000px'))
    bar.add_xaxis(company)
    bar.add_yaxis("利润率", proportion)
    bar.reversal_axis()
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    bar.set_global_opts(title_opts=opts.TitleOpts(title="利润率分析（不包括利润小于0）"))
    return bar


if __name__ == '__main__':
    handle()
