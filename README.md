<h1 align="center">pond-loach</h1>

<p align="center">
<img src="https://img.shields.io/badge/python_-%3E%3D3.8-green" alt=""> <img src="https://img.shields.io/badge/license_-MIT-green" alt=""> <img src="https://img.shields.io/badge/selenium-blue" alt=""> <img src="https://img.shields.io/badge/pyecharts-blue" alt="">  <img src="https://img.shields.io/badge/pywebio-blue" alt=""> 
</p>

## 仓库介绍

&emsp;&emsp;爬取财富网下的2021年世界五百强并作图分析, 对不同经济实力的对比

![bar](https://github.com/weiensong/pond-loach/blob/master/images/bar.png)
![pie](https://github.com/weiensong/pond-loach/blob/master/images/pie.png)

## 安装

这个项目使用[Python](https://www.python.org/) [Git](https://git-scm.com/) 请确保你本地安装了它们。

```shell
$ git clone https://github.com/weiensong/Fortune500.git
```
下载你本地[chrome](chrome://version/)浏览器对应版本的[chromedriver](https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json)

## 运行
### 创建虚拟环境并激活
```shell
python -m venv venv && source venv/bin/activate
```
### 安装依赖
```shell
pip install -r requriements.txt
```
### 爬取
```shell
python crawler.py
```
### 作图并生成html
```shell
python analyze.py
```

## 相关仓库

- [python](https://github.com/TheAlgorithms/Python) — All Algorithms implemented in Python
- [Selenium](https://github.com/SeleniumHQ/selenium) — A browser automation framework and ecosystem
- [PyWebIO](https://github.com/pywebio/PyWebIO) — Write interactive web app in script way
- [pyecharts](https://github.com/pyecharts/pyecharts) — 人人可用的开源数据可视化分析工具



## 相关链接
- [财富中文网](https://www.fortunechina.com/fortune500/c/2021-08/02/content_394571.htm)

## 维护者
[@touero](https://github.com/touero)


## 如何贡献
非常欢迎你的加入！[提一个 Issue](https://github.com/weiensong/Fortune500/issues) 或者提交一个 Pull Request。

标准 Python 遵循 [Python PEP-8](https://peps.python.org/pep-0008/) 行为规范。

### 贡献者

感谢参与项目的所有人



## 使用许可

[MIT](https://github.com/weiensong/pond-loach) © weiensong

