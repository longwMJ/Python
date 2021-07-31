import re



val = re.findall(r"\d+", '我的电话号码是: 158137...86')
# ['158137', '86']
print(val)

for i in val:
    print(i)




s = re.search(r"\d+", '我的电话号码是: 158137...86')
# <re.Match object; span=(9, 15), match='158137'>
print(s)
# 158137
print(s.group())


# 从头开始匹配, 第一个不符合要求就报错!!! 个人觉得没什么用
m = re.match(r"\d+", '86我的电话号码是: 158137...86')
# <re.Match object; span=(0, 2), match='86'>
print(m)
# 86
print(m.group())


# 预加载正则表达式 正则变量化  可以反复用

obj = re.compile(r"\d+")

redemo = obj.finditer('86我的电话号码是: 158137...86')
for j in redemo:
    print(j.group())



htmltext = """
<div class="c-row c-gap-top-small op-tieba-general-col-bottom-xs">
                                                    <div class="c-span2">
                                <a class="op-tieba-general-photo-link c-img c-img-radius-large" href="http://www.baidu.com/link?url=uvMFGV_VsBF8nhq7yJW35ukGC9If5KkAR26xWeNDGhS2fAByvDOzINTNJfwK36HxaBLHbuSU6FX5ZDBuZhjUo_" target="_blank">
                                    <span class="c-img-border c-img-radius-large"></span>
                                    <img src="https://tiebapic.baidu.com/forum/pic/item/b151f8198618367a6ab80c8d39738bd4b31ce5a9.jpg">
                                </a>
                            </div> 
                                                                            <div class="c-span10 c-span-last op-tieba-general-col-top-xs">
                                                                                                            <p class="c-color-gray2">12寓意要爱&lt;——</p>
                                                                                                                                                                                <p><span>关注用户：<span>4068</span>人</span></p>
                                        <p><span>累计发贴：<span>2万</span></span></p>
                                                                                                                                        <p>
                                                                                    <a href="http://www.baidu.com/link?url=K9lFQbKZGzVJBA92o10xji6bN0qN9lPIdsdl8WAW-bQtoGgqwZhG8xaNmvTydNLKwObX6cRFZrzbAKfaCO5MKK" class="c-gap-right-small" target="_blank">精品贴</a>
                                                                                    <a href="http://www.baidu.com/link?url=uvMFGV_VsBF8nhq7yJW35ukGC9If5KkAR26xWeNDGhUjLhenrS8GiQAz_Z_dJqe1y5tV3ukDAAoIQvbzSEnw8aU-bV51IelMOA3jNIKRiPC" class="c-gap-right-small" target="_blank">图片</a>
                                                                            </p>
                                                            </div>
                           
                    </div>
"""

# 没效果 !!!!
htmlR = re.compile(r'/<\/?[a-zA-Z]+(\s+[a-zA-Z]+=".*")*>/g')

htmlV = htmlR.finditer(htmltext)

print(htmlV)

for i in htmlV:
    print(i)



