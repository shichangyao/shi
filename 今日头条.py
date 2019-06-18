from selenium import webdriver
from lxml import etree
from pyquery import PyQuery as pq
import time

# 步骤
# 1、打开浏览器，谷歌
# 2、输入今日头条的网址
# 3、点击科技----实际上是定位元素
# 4、检查     断言设计