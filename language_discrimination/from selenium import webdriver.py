from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path=r'C:/Users/admin/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get("https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000148544&dispCatNo=1000001000100080003&trackingCd=Cat1000001000100080003_Small.html")
time.sleep(3)
result = driver.find_element_by_xpath("//*[@id=\"gdasContentsArea\"]/div/div[3]/dl[1]/dd/ul/li[1]/em")
print(result.text)