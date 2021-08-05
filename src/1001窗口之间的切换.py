from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import time

# 创建浏览器对象 
web = Chrome()

# 打开网址
web.get('https://www.lagou.com/')

# 互联网求职招聘找工作-上拉勾招聘-专业的互联网求职招聘网站
print(web.title)

# 点击某个元素 地址: 在控制台, 找到元素, 右键 copy -》 copy xPath
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')



el.click()

# 让浏览器缓一会, 加载后面的数据
time.sleep(2)


# 在搜索框输入, 回车/点击搜索按钮
elSearch = web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)


time.sleep(2)
web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()

time.sleep(2)

# 进入新窗口提取
# 注意, 在selenium里, 新窗口默认是不切换的(不跳转新的tab页面), 解决:
# 打开最后一个tab页面
web.switch_to.window(web.window_handles[-1])

# 在新窗口提取内容
# 
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text

print(job_detail)

# 关闭子窗口
web.close()

# 跳回来
web.switch_to.window(web.window_handles[0])


# 测试
# 提取数据
# 找到主要的li
elLis = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in elLis:
    # title = li.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text
    title = li.find_element_by_tag_name('h3').text
    print('title:', title)

    # err 第一个money的值都是一样, 我猜是因为li[1]固定了查找范围, 要改成./才行
    # money = li.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[2]/div/span').text


    money2 = li.find_element_by_xpath('./div[1]/div[1]/div[2]/div/span').text
    # print('money:', money)
    print('money2:', money2)

    company = li.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text

    print('company:', company)



