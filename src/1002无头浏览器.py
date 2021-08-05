from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

# 准备好无头浏览器参数配置
opt = Options()
# 无头
opt.add_argument("--headless")
# 显卡不显示
opt.add_argument("--disbale-gpu")


# web = Chrome()
web = Chrome(options=opt)

web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

# 定位里面到下拉列表
sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')

# 包装下拉列表
sel = Select(sel_el)

# 让浏览器选择对应年份(选项)

for i in range(len(sel.options)):
    # 打开对应的电影年份
    sel.select_by_index(i)
    time.sleep(2)
    table = web.find_element_by_xpath('//*[@id="TableList"]/table')
    print(table.text)
    print('===========================')
