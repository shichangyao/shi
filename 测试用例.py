from selenium import webdriver
import HTMLTestRunner
import unittest
import time

# 1、打开谷歌浏览器
# 2、输入百度
# 3、定位文本输入框，输入Python自动化测试内容
# 4、点击百度一下或者Enter键
# 5、断言设计
# 6、生成测试报告

#定义百度测试用例
class BaiduIdeTest(unittest.TestCase):
    #测试前的准备工作
    def setUp(self):
        self.driver=webdriver.Chrome("D:\Google\Chrome\Application\chromedriver.exe")#谷歌
        self.driver.implicitly_wait(30)#隐形等待，智能等待，确定内容节点完全加载
        self.base_url="https://www.baidu.com"
        time.sleep(5)

    #测试用例
    def test_baidu_ide(self):
        driver=self.driver
        driver.get(self.base_url)#2.输入百度
        driver.find_element_by_id("kw").clear()#清空默认值
        driver.find_element_by_id("kw").send_keys("python自动化")#模拟键盘
        #4.点击百度一下，或者enter键
        driver.find_element_by_id("su").click()#点击
        time.sleep(5)
        #断言设计
        self.assertEqual("python自动化_百度搜索",driver.title)


    #测试之后的一起清除工作，资源释放
    def tearDown(self):
        self.driver.quit()#退出浏览器

#生成测试报告
if __name__=='__main__':
    testsuit=unittest.TestSuite()#添加测试套件
    testsuit.addTest(BaiduIdeTest("test_baidu_ide"))#测试用例添加到测试套件中
    fp=open('./result.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title='自动化测试报告',
                                         description='用例执行情况')
    runner.run(testsuit)#运行
    fp.close()#关闭
#with open() as if: 自动关闭