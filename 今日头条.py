from selenium import webdriver
from lxml import etree
from pyquery import PyQuery as pq
import time

# 步骤
# 1、打开浏览器，谷歌
# 2、输入今日头条的网址
# 3、点击科技----实际上是定位元素
# 4、检查     断言设计
driver=webdriver.Chrome("D:\Google\Chrome\Application\chromedriver.exe")#谷歌
driver.get("https://www.toutiao.com")
driver.implicitly_wait(30)
driver.find_element_by_link_text("科技").click()
time.sleep(5)


for i in range(3):
    js="var q=document.documentElement.scrollTop="+str(i*500)#控制滚动条位置
    driver.execute_script(js)#执行js
    time.sleep(2)
#  #100000  滚动条最下方   0   最上方   决定滚动条的位置
#  js="var q = document.documentElement.scrollTop=100000"
page=driver.page_source#获取网页源码
doc=pq(page)#实例化一下
doc=etree.HTML(str(doc))#构造xpath解析对象
contents=doc.xpath('//div[@class="wcommonFeed"]/ul/li')

for x in contents:
    title=x.xpath("div/div[1]/div/div[1]/a/text()")
    print(title)
    #断言
driver.quit()#退出