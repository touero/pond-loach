import csv
from pyecharts.charts import Bar, Pie, Page
from pyecharts import options as opts


def load_fortune_data():
    nation_dict = {}
    company = []
    income = []
    profit = []
    proportion = []

    with open(r'Fortune500After.csv', encoding='utf-8') as jd:
        for i in range(1):
            jd.readline()  # 跳过第一行
        for row in csv.reader(jd):
            try:
                # 获取国家数据
                if row[4] not in nation_dict:
                    nation_dict[row[4]] = 1
                else:
                    nation_dict[row[4]] += 1

                # 获取公司收入和利润数据
                if float(row[3]) > 0:
                    company.append(row[1])
                    income.append(float(row[2]))
                    profit.append(float(row[3]))
                    proportion.append(float(row[3]) / float(row[2]) * 100)
            except Exception as e:
                print(e)

    return nation_dict, company, income, profit, proportion


nation_dict, company, income, profit, proportion = load_fortune_data()


# 创建各个图表
def create_proportion_bar():
    nation_value_list = [nation_dict[key] for key in nation_dict]
    nation_key_list = list(nation_dict.keys())
    bar = Bar()
    bar.add_xaxis(nation_key_list)
    bar.add_yaxis("世界500强数量", nation_value_list)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="各个国家拥有世界500强企业"),
                        xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 45}))
    return bar


def create_proportion_pie():
    nation_value_list = [nation_dict[key] for key in nation_dict]
    nation_key_list = list(nation_dict.keys())
    pie = Pie()
    pie.add('数量', [list(z) for z in zip(nation_key_list, nation_value_list)], radius='45%', center=["50%", "65%"])
    return pie


def create_income_profit():
    bar = Bar(init_opts=opts.InitOpts(width='4000px', height='30000px'))
    bar.add_xaxis(company)
    bar.add_yaxis("营业收入", income)
    bar.add_yaxis("利润", profit)
    bar.reversal_axis()
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    bar.set_global_opts(title_opts=opts.TitleOpts(title="营业收入与利润（不包括利润小于0）"))
    return bar


def create_proportion():
    bar = Bar(init_opts=opts.InitOpts(width='4000px', height='30000px'))
    bar.add_xaxis(company)
    bar.add_yaxis("利润率", proportion)
    bar.reversal_axis()
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    bar.set_global_opts(title_opts=opts.TitleOpts(title="利润率分析（不包括利润小于0）"))
    return bar


# 创建HTML文件
def save_all_charts():
    # 创建页面并添加图表
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        create_proportion_bar(),
        create_proportion_pie(),
        create_income_profit(),
        create_proportion()
    )

    # 修复：转义花括号，避免格式化占位符冲突
    html_content = f'''
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Fortune 500 数据分析</title>
        <script type="text/javascript">
            function showChart(chartId) {{
                // 隐藏所有图表
                var charts = document.getElementsByClassName('chart');
                for (var i = 0; i < charts.length; i++) {{
                    charts[i].style.display = 'none';
                }}
                // 显示选中的图表
                document.getElementById(chartId).style.display = 'block';
            }}
        </script>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
            }}
            .chart-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                margin-bottom: 40px;
            }}
            .chart {{
                width: 80%;
                height: 500px;
                display: none;
            }}
            button {{
                margin: 10px;
                padding: 10px;
                font-size: 16px;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <h1>Fortune 500 数据分析</h1>
        <div style="text-align:center; margin-bottom: 20px;">
            <button onclick="showChart('bar-chart')">世界500强数量（条形图）</button>
            <button onclick="showChart('pie-chart')">世界500强数量（饼图）</button>
            <button onclick="showChart('income-profit-chart')">营业收入与利润</button>
            <button onclick="showChart('proportion-chart')">利润率分析</button>
        </div>
        <div class="chart-container">
            <div id="bar-chart" class="chart">
                {create_proportion_bar().render_embed()}
            </div>
        </div>
        <div class="chart-container">
            <div id="pie-chart" class="chart">
                {create_proportion_pie().render_embed()}
            </div>
        </div>
        <div class="chart-container">
            <div id="income-profit-chart" class="chart">
                {create_income_profit().render_embed()}
            </div>
        </div>
        <div class="chart-container">
            <div id="proportion-chart" class="chart">
                {create_proportion().render_embed()}
            </div>
        </div>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5.3.3/dist/echarts.min.js"></script>
    </body>
    </html>
    '''

    # 保存为HTML文件
    with open("fortune500_charts_with_menu.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("fortune500_charts_with_menu.html 保存成功！")


if __name__ == '__main__':
    save_all_charts()
