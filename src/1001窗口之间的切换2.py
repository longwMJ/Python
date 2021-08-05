from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import time

# 创建浏览器对象
web = Chrome()

v_url = 'https://www.91kanju.com/vod-play/541-1-1.html'

# 打开网址 如果页面遇到iframe该如何处理
web.get(v_url)


time.sleep(10)

# 处理iframe, 必须先找到iframe, 然后切换视角到iframe, 再然后才可以拿到数据
iframe = web.find_element_by_xpath('//*[@id="player_iframe"]')
web.switch_to.frame(iframe)


# 没成功~~~
iframe_text = web.find_element_by_xpath('/html/head/title').text

print(iframe_text)

# 切换回去
# web.switch_to.default_content()
