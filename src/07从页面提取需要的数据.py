import re
import requests
import csv

print('king')

url = 'https://movie.douban.com/top250'

newheaders = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

res = requests.get(url, headers=newheaders)

# 原html代码在底部
resText = res.text

# print(resText)

# 解析数据

# obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)

# obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)'
#                  r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp*?', re.S)

# obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)'
#                  r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
#                  r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>', re.S)


# obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)'
#                  r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
#                  r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>', re.S)

obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<numRen>.*?)人评价</span>', re.S)

resFind = obj.finditer(resText)

f = open("data.csv", mode="w")

csWriter = csv.writer(f)

for i in resFind:
    print(i.group("name"))
    print(i.group("score"))
    print(i.group("numRen"))
    print(i.group("year").strip())

    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csWriter.writerow(dic.values())


f.close()
res.close()
print('over')


# html   :


# <body >

#     <script type = "text/javascript" > var _body_start = new Date(); < /script >

#     <link href = "//img3.doubanio.com/dae/accounts/resources/d3e2921/shire/bundle.css" rel = "stylesheet" type = "text/css" >


# <div id = "db-global-nav" class = "global-nav" >
#   <div class = "bd" >

# <div class = "top-nav-info" >
#   <a href = "https://accounts.douban.com/passport/login?source=movie" class = "nav-login" rel = "nofollow" > 登录/注册 < /a >
# </div >

#     <div class = "top-nav-doubanapp" >
#   <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
#   <div id="doubanapp-tip">
#     <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
#     <a href="javascript: void 0;" class="tip-close">×</a>
#   </div>
#   <div id="top-nav-appintro" class="more-items">
#     <p class="appintro-title">豆瓣</p>
#     <p class="qrcode">扫码直接下载</p>
#     <div class="download">
#       <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&amp;direct_dl=1&amp;download=iOS">iPhone</a>
#       <span>·</span>
#       <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&amp;direct_dl=1&amp;download=Android" class="download-android">Android</a>
#     </div>
#   </div>
# </div>

    


# <div class="global-nav-items">
#   <ul>
#     <li class="">
#       <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
#     </li>
#     <li class="">
#       <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
#     </li>
#     <li class="on">
#       <a href="https://movie.douban.com" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
#     </li>
#     <li class="">
#       <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
#     </li>
#     <li class="">
#       <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
#     </li>
#     <li class="">
#       <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
#     </li>
#     <li class="">
#       <a href="https://read.douban.com/?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
#     </li>
#     <li class="">
#       <a href="https://douban.fm/?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
#     </li>
#     <li class="">
#       <a href="https://time.douban.com/?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
#     </li>
#     <li class="">
#       <a href="https://market.douban.com/?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
#     </li>
#   </ul>
# </div>

#   </div>
# </div>
# <script>
#   ;window._GLOBAL_NAV = {
#     DOUBAN_URL: "https://www.douban.com",
#     N_NEW_NOTIS: 0,
#     N_NEW_DOUMAIL: 0
#   };
# </script>



#     <script src="//img3.doubanio.com/dae/accounts/resources/d3e2921/shire/bundle.js" defer="defer"></script>




    



#     <link href="//img3.doubanio.com/dae/accounts/resources/d3e2921/movie/bundle.css" rel="stylesheet" type="text/css">




# <div id="db-nav-movie" class="nav">
#   <div class="nav-wrap">
#   <div class="nav-primary">
#     <div class="nav-logo">
#       <a href="https://movie.douban.com">豆瓣电影</a>
#     </div>
#     <div class="nav-search">
#       <form action="https://search.douban.com/movie/subject_search" method="get">
#         <fieldset>
#           <legend>搜索：</legend>
#           <label for="inp-query">
#           </label>
#           <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value="" autocomplete="off"></div>
#           <div class="inp-btn"><input type="submit" value="搜索"></div>
#           <input type="hidden" name="cat" value="1002">
#         </fieldset>
#       </form>
#     </div>
#   </div>
#   </div>
#   <div class="nav-secondary">
    

# <div class="nav-items">
#   <ul>
#     <li><a href="https://movie.douban.com/cinema/nowplaying/">影讯&amp;购票</a>
#     </li>
#     <li><a href="https://movie.douban.com/explore">选电影</a>
#     </li>
#     <li><a href="https://movie.douban.com/tv/">电视剧</a>
#     </li>
#     <li><a href="https://movie.douban.com/chart">排行榜</a>
#     </li>
#     <li><a href="https://movie.douban.com/tag/">分类</a>
#     </li>
#     <li><a href="https://movie.douban.com/review/best/">影评</a>
#     </li>
#     <li><a href="https://movie.douban.com/annual/2020?source=navigation">2020年度榜单</a>
#     </li>
#     <li><a href="https://www.douban.com/standbyme/2020?fullscreen=true&amp;hidenav=true&amp;autorotate=false&amp;source=movie_navigation" target="_blank">2020书影音报告</a>
#     </li>
#   </ul>
# </div>

#     <a href="https://movie.douban.com/annual/2020?source=movie_navigation" class="movieannual"></a>
#   </div>
# </div>

# <script id="suggResult" type="text/x-jquery-tmpl">
#   <li data-link="{{= url}}">
#             <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
#             <img src="{{= img}}" width="40" />
#             <p>
#                 <em>{{= title}}</em>
#                 {{if year}}
#                     <span>{{= year}}</span>
#                 {{/if}}
#                 {{if sub_title}}
#                     <br /><span>{{= sub_title}}</span>
#                 {{/if}}
#                 {{if address}}
#                     <br /><span>{{= address}}</span>
#                 {{/if}}
#                 {{if episode}}
#                     {{if episode=="unknow"}}
#                         <br /><span>集数未知</span>
#                     {{else}}
#                         <br /><span>共{{= episode}}集</span>
#                     {{/if}}
#                 {{/if}}
#             </p>
#         </a>
#         </li>
#   </script>




#     <script src="//img3.doubanio.com/dae/accounts/resources/d3e2921/movie/bundle.js" defer="defer"></script>





    
#     <div id="wrapper">
        

        
#     <div id="content">
        
#     <h1>豆瓣电影 Top 250</h1>

#         <div class="grid-16-8 clearfix">
            
            
#             <div class="article">
                







# <div class="opt mod">
#     <div class="tabs">
      
    

#     </div>
#     <span id="mine-selector">
#       <input type="checkbox" value="unwatched">我没看过的
#     </span>
# </div>



# <ol class="grid_view">
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">1</em>
#                     <a href="https://movie.douban.com/subject/1292052/">
#                         <img width="100" alt="肖申克的救赎" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1292052/" class="">
#                             <span class="title">肖申克的救赎</span>
#                                     <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
#                                 <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
#                             1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating5-t"></span>
#                                 <span class="rating_num" property="v:average">9.7</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>2407985人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">希望让人自由。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">2</em>
#                     <a href="https://movie.douban.com/subject/1291546/">
#                         <img width="100" alt="霸王别姬" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2561716440.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1291546/" class="">
#                             <span class="title">霸王别姬</span>
#                                 <span class="other">&nbsp;/&nbsp;再见，我的妾  /  Farewell My Concubine</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 陈凯歌 Kaige Chen&nbsp;&nbsp;&nbsp;主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...<br>
#                             1993&nbsp;/&nbsp;中国大陆 中国香港&nbsp;/&nbsp;剧情 爱情 同性
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating5-t"></span>
#                                 <span class="rating_num" property="v:average">9.6</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1792162人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">风华绝代。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">3</em>
#                     <a href="https://movie.douban.com/subject/1292720/">
#                         <img width="100" alt="阿甘正传" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2372307693.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1292720/" class="">
#                             <span class="title">阿甘正传</span>
#                                     <span class="title">&nbsp;/&nbsp;Forrest Gump</span>
#                                 <span class="other">&nbsp;/&nbsp;福雷斯特·冈普</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 罗伯特·泽米吉斯 Robert Zemeckis&nbsp;&nbsp;&nbsp;主演: 汤姆·汉克斯 Tom Hanks / ...<br>
#                             1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 爱情
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating5-t"></span>
#                                 <span class="rating_num" property="v:average">9.5</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1812564人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">一部美国近现代史。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">4</em>
#                     <a href="https://movie.douban.com/subject/1295644/">
#                         <img width="100" alt="这个杀手不太冷" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p511118051.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1295644/" class="">
#                             <span class="title">这个杀手不太冷</span>
#                                     <span class="title">&nbsp;/&nbsp;Léon</span>
#                                 <span class="other">&nbsp;/&nbsp;杀手莱昂  /  终极追杀令(台)</span>
#                         </a>


#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 吕克·贝松 Luc Besson&nbsp;&nbsp;&nbsp;主演: 让·雷诺 Jean Reno / 娜塔莉·波特曼 ...<br>
#                             1994&nbsp;/&nbsp;法国 美国&nbsp;/&nbsp;剧情 动作 犯罪
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.4</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1981022人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">怪蜀黍和小萝莉不得不说的故事。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">5</em>
#                     <a href="https://movie.douban.com/subject/1292722/">
#                         <img width="100" alt="泰坦尼克号" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p457760035.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1292722/" class="">
#                             <span class="title">泰坦尼克号</span>
#                                     <span class="title">&nbsp;/&nbsp;Titanic</span>
#                                 <span class="other">&nbsp;/&nbsp;铁达尼号(港 / 台)</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 詹姆斯·卡梅隆 James Cameron&nbsp;&nbsp;&nbsp;主演: 莱昂纳多·迪卡普里奥 Leonardo...<br>
#                             1997&nbsp;/&nbsp;美国 墨西哥 澳大利亚 加拿大&nbsp;/&nbsp;剧情 爱情 灾难
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.4</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1773872人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">失去的才是永恒的。 </span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">6</em>
#                     <a href="https://movie.douban.com/subject/1292063/">
#                         <img width="100" alt="美丽人生" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2578474613.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1292063/" class="">
#                             <span class="title">美丽人生</span>
#                                     <span class="title">&nbsp;/&nbsp;La vita è bella</span>
#                                 <span class="other">&nbsp;/&nbsp;一个快乐的传说(港)  /  Life Is Beautiful</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 罗伯托·贝尼尼 Roberto Benigni&nbsp;&nbsp;&nbsp;主演: 罗伯托·贝尼尼 Roberto Beni...<br>
#                             1997&nbsp;/&nbsp;意大利&nbsp;/&nbsp;剧情 喜剧 爱情 战争
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating5-t"></span>
#                                 <span class="rating_num" property="v:average">9.6</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1112025人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">最美的谎言。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">7</em>
#                     <a href="https://movie.douban.com/subject/1291561/">
#                         <img width="100" alt="千与千寻" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2557573348.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1291561/" class="">
#                             <span class="title">千与千寻</span>
#                                     <span class="title">&nbsp;/&nbsp;千と千尋の神隠し</span>
#                                 <span class="other">&nbsp;/&nbsp;神隐少女(台)  /  千与千寻的神隐</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 宫崎骏 Hayao Miyazaki&nbsp;&nbsp;&nbsp;主演: 柊瑠美 Rumi Hîragi / 入野自由 Miy...<br>
#                             2001&nbsp;/&nbsp;日本&nbsp;/&nbsp;剧情 动画 奇幻
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.4</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1890830人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">最好的宫崎骏，最好的久石让。 </span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">8</em>
#                     <a href="https://movie.douban.com/subject/1295124/">
#                         <img width="100" alt="辛德勒的名单" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p492406163.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1295124/" class="">
#                             <span class="title">辛德勒的名单</span>
#                                     <span class="title">&nbsp;/&nbsp;Schindler's List</span>
#                                 <span class="other">&nbsp;/&nbsp;舒特拉的名单(港)  /  辛德勒名单</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 史蒂文·斯皮尔伯格 Steven Spielberg&nbsp;&nbsp;&nbsp;主演: 连姆·尼森 Liam Neeson...<br>
#                             1993&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 历史 战争
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating5-t"></span>
#                                 <span class="rating_num" property="v:average">9.5</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>924488人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">拯救一个人，就是拯救整个世界。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">9</em>
#                     <a href="https://movie.douban.com/subject/3541415/">
#                         <img width="100" alt="盗梦空间" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2616355133.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/3541415/" class="">
#                             <span class="title">盗梦空间</span>
#                                     <span class="title">&nbsp;/&nbsp;Inception</span>
#                                 <span class="other">&nbsp;/&nbsp;潜行凶间(港)  /  全面启动(台)</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 克里斯托弗·诺兰 Christopher Nolan&nbsp;&nbsp;&nbsp;主演: 莱昂纳多·迪卡普里奥 Le...<br>
#                             2010&nbsp;/&nbsp;美国 英国&nbsp;/&nbsp;剧情 科幻 悬疑 冒险
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.3</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1744811人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">诺兰给了我们一场无法盗取的梦。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">10</em>
#                     <a href="https://movie.douban.com/subject/3011091/">
#                         <img width="100" alt="忠犬八公的故事" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p524964039.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/3011091/" class="">
#                             <span class="title">忠犬八公的故事</span>
#                                     <span class="title">&nbsp;/&nbsp;Hachi: A Dog's Tale</span>
#                                 <span class="other">&nbsp;/&nbsp;秋田犬八千(港)  /  忠犬小八(台)</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 莱塞·霍尔斯道姆 Lasse Hallström&nbsp;&nbsp;&nbsp;主演: 理查·基尔 Richard Ger...<br>
#                             2009&nbsp;/&nbsp;美国 英国&nbsp;/&nbsp;剧情
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.4</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1199629人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">永远都不能忘记你所爱的人。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">11</em>
#                     <a href="https://movie.douban.com/subject/1889243/">
#                         <img width="100" alt="星际穿越" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2614988097.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1889243/" class="">
#                             <span class="title">星际穿越</span>
#                                     <span class="title">&nbsp;/&nbsp;Interstellar</span>
#                                 <span class="other">&nbsp;/&nbsp;星际启示录(港)  /  星际效应(台)</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 克里斯托弗·诺兰 Christopher Nolan&nbsp;&nbsp;&nbsp;主演: 马修·麦康纳 Matthew Mc...<br>
#                             2014&nbsp;/&nbsp;美国 英国 加拿大&nbsp;/&nbsp;剧情 科幻 冒险
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.3</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1418422人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">爱是一种力量，让我们超越时空感知它的存在。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">12</em>
#                     <a href="https://movie.douban.com/subject/1292064/">
#                         <img width="100" alt="楚门的世界" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p479682972.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1292064/" class="">
#                             <span class="title">楚门的世界</span>
#                                     <span class="title">&nbsp;/&nbsp;The Truman Show</span>
#                                 <span class="other">&nbsp;/&nbsp;真人Show(港)  /  真人戏</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 彼得·威尔 Peter Weir&nbsp;&nbsp;&nbsp;主演: 金·凯瑞 Jim Carrey / 劳拉·琳妮 Lau...<br>
#                             1998&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 科幻
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.3</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1337609人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">如果再也不能见到你，祝你早安，午安，晚安。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">13</em>
#                     <a href="https://movie.douban.com/subject/1292001/">
#                         <img width="100" alt="海上钢琴师" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2574551676.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1292001/" class="">
#                             <span class="title">海上钢琴师</span>
#                                     <span class="title">&nbsp;/&nbsp;La leggenda del pianista sull'oceano</span>
#                                 <span class="other">&nbsp;/&nbsp;声光伴我飞(港)  /  一九零零的传奇</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 朱塞佩·托纳多雷 Giuseppe Tornatore&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗斯 Tim Roth / ...<br>
#                             1998&nbsp;/&nbsp;意大利&nbsp;/&nbsp;剧情 音乐
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.3</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1417920人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">每个人都要走一条自己坚定了的路，就算是粉身碎骨。 </span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">14</em>
#                     <a href="https://movie.douban.com/subject/3793023/">
#                         <img width="100" alt="三傻大闹宝莱坞" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p579729551.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/3793023/" class="">
#                             <span class="title">三傻大闹宝莱坞</span>
#                                     <span class="title">&nbsp;/&nbsp;3 Idiots</span>
#                                 <span class="other">&nbsp;/&nbsp;三个傻瓜(台)  /  作死不离3兄弟(港)</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 拉库马·希拉尼 Rajkumar Hirani&nbsp;&nbsp;&nbsp;主演: 阿米尔·汗 Aamir Khan / 卡...<br>
#                             2009&nbsp;/&nbsp;印度&nbsp;/&nbsp;剧情 喜剧 爱情 歌舞
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.2</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1591481人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">英俊版憨豆，高情商版谢耳朵。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">15</em>
#                     <a href="https://movie.douban.com/subject/2131459/">
#                         <img width="100" alt="机器人总动员" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1461851991.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/2131459/" class="">
#                             <span class="title">机器人总动员</span>
#                                     <span class="title">&nbsp;/&nbsp;WALL·E</span>
#                                 <span class="other">&nbsp;/&nbsp;太空奇兵·威E(港)  /  瓦力(台)</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 安德鲁·斯坦顿 Andrew Stanton&nbsp;&nbsp;&nbsp;主演: 本·贝尔特 Ben Burtt / 艾丽...<br>
#                             2008&nbsp;/&nbsp;美国&nbsp;/&nbsp;科幻 动画 冒险
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.3</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1119696人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">小瓦力，大人生。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">16</em>
#                     <a href="https://movie.douban.com/subject/1291549/">
#                         <img width="100" alt="放牛班的春天" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1910824951.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1291549/" class="">
#                             <span class="title">放牛班的春天</span>
#                                     <span class="title">&nbsp;/&nbsp;Les choristes</span>
#                                 <span class="other">&nbsp;/&nbsp;歌声伴我心(港)  /  唱诗班男孩</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 克里斯托夫·巴拉蒂 Christophe Barratier&nbsp;&nbsp;&nbsp;主演: 热拉尔·朱尼奥 Gé...<br>
#                             2004&nbsp;/&nbsp;法国 瑞士 德国&nbsp;/&nbsp;剧情 喜剧 音乐
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.3</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1104744人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">天籁一般的童声，是最接近上帝的存在。 </span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">17</em>
#                     <a href="https://movie.douban.com/subject/1307914/">
#                         <img width="100" alt="无间道" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2564556863.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1307914/" class="">
#                             <span class="title">无间道</span>
#                                     <span class="title">&nbsp;/&nbsp;無間道</span>
#                                 <span class="other">&nbsp;/&nbsp;Infernal Affairs  /  Mou gaan dou</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 刘伟强 / 麦兆辉&nbsp;&nbsp;&nbsp;主演: 刘德华 / 梁朝伟 / 黄秋生<br>
#                             2002&nbsp;/&nbsp;中国香港&nbsp;/&nbsp;剧情 犯罪 惊悚
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.3</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1083287人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">香港电影史上永不过时的杰作。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">18</em>
#                     <a href="https://movie.douban.com/subject/25662329/">
#                         <img width="100" alt="疯狂动物城" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2614500649.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/25662329/" class="">
#                             <span class="title">疯狂动物城</span>
#                                     <span class="title">&nbsp;/&nbsp;Zootopia</span>
#                                 <span class="other">&nbsp;/&nbsp;优兽大都会(港)  /  动物方城市(台)</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 拜伦·霍华德 Byron Howard / 瑞奇·摩尔 Rich Moore&nbsp;&nbsp;&nbsp;主演: 金妮弗·...<br>
#                             2016&nbsp;/&nbsp;美国&nbsp;/&nbsp;喜剧 动画 冒险
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.2</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1568266人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">迪士尼给我们营造的乌托邦就是这样，永远善良勇敢，永远出乎意料。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">19</em>
#                     <a href="https://movie.douban.com/subject/1292213/">
#                         <img width="100" alt="大话西游之大圣娶亲" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2455050536.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1292213/" class="">
#                             <span class="title">大话西游之大圣娶亲</span>
#                                     <span class="title">&nbsp;/&nbsp;西遊記大結局之仙履奇緣</span>
#                                 <span class="other">&nbsp;/&nbsp;西游记完结篇仙履奇缘  /  齐天大圣西游记</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 刘镇伟 Jeffrey Lau&nbsp;&nbsp;&nbsp;主演: 周星驰 Stephen Chow / 吴孟达 Man Tat Ng...<br>
#                             1995&nbsp;/&nbsp;中国香港 中国大陆&nbsp;/&nbsp;喜剧 爱情 奇幻 古装
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.2</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1291219人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">一生所爱。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">20</em>
#                     <a href="https://movie.douban.com/subject/5912992/">
#                         <img width="100" alt="熔炉" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1363250216.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/5912992/" class="">
#                             <span class="title">熔炉</span>
#                                     <span class="title">&nbsp;/&nbsp;도가니</span>
#                                 <span class="other">&nbsp;/&nbsp;无声呐喊(港)  /  漩涡</span>
#                         </a>


#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 黄东赫 Dong-hyuk Hwang&nbsp;&nbsp;&nbsp;主演: 孔侑 Yoo Gong / 郑有美 Yu-mi Jung /...<br>
#                             2011&nbsp;/&nbsp;韩国&nbsp;/&nbsp;剧情
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.3</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>783216人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">我们一路奋战不是为了改变世界，而是为了不让世界改变我们。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">21</em>
#                     <a href="https://movie.douban.com/subject/1291841/">
#                         <img width="100" alt="教父" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p616779645.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1291841/" class="">
#                             <span class="title">教父</span>
#                                     <span class="title">&nbsp;/&nbsp;The Godfather</span>
#                                 <span class="other">&nbsp;/&nbsp;Mario Puzo's The Godfather</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 弗朗西斯·福特·科波拉 Francis Ford Coppola&nbsp;&nbsp;&nbsp;主演: 马龙·白兰度 M...<br>
#                             1972&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 犯罪
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.3</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>786464人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">千万不要记恨你的对手，这样会让你失去理智。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">22</em>
#                     <a href="https://movie.douban.com/subject/1849031/">
#                         <img width="100" alt="当幸福来敲门" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2614359276.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1849031/" class="">
#                             <span class="title">当幸福来敲门</span>
#                                     <span class="title">&nbsp;/&nbsp;The Pursuit of Happyness</span>
#                                 <span class="other">&nbsp;/&nbsp;寻找快乐的故事(港)  /  追求快乐</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 加布里尔·穆奇诺 Gabriele Muccino&nbsp;&nbsp;&nbsp;主演: 威尔·史密斯 Will Smith ...<br>
#                             2006&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 传记 家庭
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.1</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1280335人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">平民励志片。 </span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">23</em>
#                     <a href="https://movie.douban.com/subject/1291560/">
#                         <img width="100" alt="龙猫" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2540924496.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1291560/" class="">
#                             <span class="title">龙猫</span>
#                                     <span class="title">&nbsp;/&nbsp;となりのトトロ</span>
#                                 <span class="other">&nbsp;/&nbsp;邻居托托罗  /  邻家的豆豆龙</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 宫崎骏 Hayao Miyazaki&nbsp;&nbsp;&nbsp;主演: 日高法子 Noriko Hidaka / 坂本千夏 Ch...<br>
#                             1988&nbsp;/&nbsp;日本&nbsp;/&nbsp;动画 奇幻 冒险
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.2</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1069505人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">人人心中都有个龙猫，童年就永远不会消失。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">24</em>
#                     <a href="https://movie.douban.com/subject/3319755/">
#                         <img width="100" alt="怦然心动" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p501177648.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/3319755/" class="">
#                             <span class="title">怦然心动</span>
#                                     <span class="title">&nbsp;/&nbsp;Flipped</span>
#                                 <span class="other">&nbsp;/&nbsp;萌动青春  /  青春萌动</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 罗伯·莱纳 Rob Reiner&nbsp;&nbsp;&nbsp;主演: 玛德琳·卡罗尔 Madeline Carroll / 卡...<br>
#                             2010&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 喜剧 爱情
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating45-t"></span>
#                                 <span class="rating_num" property="v:average">9.1</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1522111人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">真正的幸福是来自内心深处。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
#         <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">25</em>
#                     <a href="https://movie.douban.com/subject/1296141/">
#                         <img width="100" alt="控方证人" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1505392928.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1296141/" class="">
#                             <span class="title">控方证人</span>
#                                     <span class="title">&nbsp;/&nbsp;Witness for the Prosecution</span>
#                                 <span class="other">&nbsp;/&nbsp;雄才伟略  /  情妇</span>
#                         </a>


#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 比利·怀尔德 Billy Wilder&nbsp;&nbsp;&nbsp;主演: 泰隆·鲍华 Tyrone Power / 玛琳·...<br>
#                             1957&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 犯罪 悬疑
#                         </p>

                        
#                         <div class="star">
#                                 <span class="rating5-t"></span>
#                                 <span class="rating_num" property="v:average">9.6</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>383550人评价</span>
#                         </div>

#                             <p class="quote">
#                                 <span class="inq">比利·怀德满分作品。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
# </ol>



    
    
    

#         <div class="paginator">
#         <span class="prev">
#             &lt;前页
#         </span>
        
        

#                 <span class="thispage">1</span>
                
#             <a href="?start=25&amp;filter=">2</a>
        
                
#             <a href="?start=50&amp;filter=">3</a>
        
                
#             <a href="?start=75&amp;filter=">4</a>
        
                
#             <a href="?start=100&amp;filter=">5</a>
        
                
#             <a href="?start=125&amp;filter=">6</a>
        
                
#             <a href="?start=150&amp;filter=">7</a>
        
                
#             <a href="?start=175&amp;filter=">8</a>
        
                
#             <a href="?start=200&amp;filter=">9</a>
        
                
#             <a href="?start=225&amp;filter=">10</a>
        
#         <span class="next">
#             <link rel="next" href="?start=25&amp;filter=">
#             <a href="?start=25&amp;filter=">后页&gt;</a>
#         </span>

#             <span class="count">(共250条)</span>
#         </div>



#             </div>
#             <div class="aside">
                
# <p class="pl">
#     豆瓣用户每天都在对“看过”的电影进行“很差”到“力荐”的评价，豆瓣根据每部影片看过的人数以及该影片所得的评价等综合数据，通过算法分析产生豆瓣电影 Top 250。
# </p>

# <div id="dale_movie_top250_bottom_right" ad-status="appended" data-sell-type="RTB" data-type="GoogleRender" data-version="3.2.31"><div style="position: relative; margin: 0px 0px 20px; display: block; overflow: hidden;"><div id="dale_movie_top250_bottom_right_frame"><script src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:inline-block;width:300px;height:250px" data-ad-client="ca-pub-4830389020085397" data-ad-slot="1983604743" data-adsbygoogle-status="done" data-ad-status="filled"><ins id="aswift_0_expand" style="display:inline-table;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_0_anchor" style="display:block;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;"><iframe id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0;width:300px;height:250px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="300" height="250" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-4830389020085397&amp;output=html&amp;h=250&amp;slotname=1983604743&amp;adk=2656724884&amp;adf=367891091&amp;pi=t.ma~as.1983604743&amp;w=300&amp;lmt=1627788578&amp;psa=1&amp;format=300x250&amp;url=https%3A%2F%2Fmovie.douban.com%2Ftop250&amp;flash=0&amp;wgl=1&amp;uach=WyJtYWNPUyIsIjEwXzE1XzciLCJ4ODYiLCIiLCI5Mi4wLjQ1MTUuMTA3IixbXSxudWxsLG51bGwsbnVsbF0.&amp;tt_state=W3siaXNzdWVyT3JpZ2luIjoiaHR0cHM6Ly9hdHRlc3RhdGlvbi5hbmRyb2lkLmNvbSIsInN0YXRlIjo3fV0.&amp;dt=1627788578602&amp;bpp=6&amp;bdt=1798&amp;idt=56&amp;shv=r20210728&amp;mjsv=m202107290101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3D10f2af77a1ea3866-220684e835c60045%3AT%3D1614740879%3ART%3D1614740879%3AS%3DALNI_MYfycbmdCJOTfOnNxwELjLoRpefYQ&amp;correlator=2048992231746&amp;frm=20&amp;pv=2&amp;ga_vid=1219040786.1616633654&amp;ga_sid=1627788578&amp;ga_hid=38252945&amp;ga_fc=1&amp;u_tz=480&amp;u_his=5&amp;u_java=0&amp;u_h=1120&amp;u_w=1792&amp;u_ah=1011&amp;u_aw=1792&amp;u_cd=30&amp;u_nplug=3&amp;u_nmime=4&amp;adx=1109&amp;ady=328&amp;biw=1777&amp;bih=932&amp;scr_x=0&amp;scr_y=0&amp;eid=20211866%2C21065725%2C21067496&amp;oid=3&amp;pvsid=407474137959711&amp;pem=875&amp;eae=0&amp;fc=896&amp;brdim=0%2C109%2C0%2C109%2C1792%2C25%2C1792%2C1011%2C1792%2C932&amp;vis=1&amp;rsz=%7C%7CoeE%7C&amp;abl=CS&amp;pfx=0&amp;fu=0&amp;bc=31&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;xpc=ja2wm9qnFT&amp;p=https%3A//movie.douban.com&amp;dtd=109" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!1" data-google-query-id="CNvejYDxjvICFRmHlgodtj0GzQ" data-load-complete="true"></iframe></ins></ins></ins><script>
# (adsbygoogle = window.adsbygoogle || []).push({});
# </script><script src="https://erebor.douban.com/count/?ad=204134&amp;bid=oi6GMJ3oAuw&amp;chicken=89586c8b205e9191290748fa8aa078ad&amp;crtr=3%3A%2Ftop250&amp;device=100&amp;experiment_id=0&amp;fv=&amp;hit_word=&amp;hn=brand33&amp;lat=0.00000&amp;lon=0.00000&amp;mark=&amp;model=&amp;net=&amp;ns=1627788578387940915&amp;os=51&amp;osv=X+10_15_7&amp;p=0&amp;pid=debug_4322794cf419e9eb2931db818c7d126093471dc1&amp;price=TITDjNM8_pF57taxshxwGg&amp;rexxar=0&amp;type=impression&amp;uid=&amp;unit=dale_movie_top250_bottom_right&amp;user_variation=&amp;vendor="></script></div><div style="line-height: 1; text-align: center; background-color: rgba(0, 0, 0, 0.3); font-size: 12px; position: absolute; right: 0px; bottom: 0px; padding: 4px; color: rgb(255, 255, 255);">由谷歌提供的广告</div></div></div>

# <!-- douban ad begin -->






# <div class="mobile-app-entrance block5 app-movie">
#     <a class="entrance-link" href="https://www.douban.com/doubanapp/frodo">
#         <div class="entrance-qrcode">
#             <img src="https://img3.doubanio.com/f/movie/a02f6ed325fc52e220f299d51e730c422e2bcd16/pics/movie/douban_app_ad/qrcode.png" alt="扫码下载豆瓣 App" width="80" height="80">
#         </div>
#         <div class="entrance-info">
#             <span class="app-icon icon-movie"></span>
#             <span class="main-title">豆瓣</span>
#             <span class="sub-title">让好电影来找你</span>
#         </div>
#     </a>
# </div>

# <!-- douban ad end -->


#             </div>
#             <div class="extra">
                
#             </div>
#         </div>
#     </div>

        
#     <div id="footer">
#             <div class="footer-extra"></div>
        
# <span id="icp" class="fleft gray-link">
#     © 2005－2021 douban.com, all rights reserved 北京豆网科技有限公司
# </span>

# <a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

# <span class="fright">
#     <a href="https://www.douban.com/about">关于豆瓣</a>
#     · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
#     · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
#     · <a href="https://www.douban.com/about/legal">法律声明</a>
    
#     · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
#     · <a href="https://www.douban.com/doubanapp/">移动应用</a>
#     · <a href="https://www.douban.com/partner/">豆瓣广告</a>
# </span>

#     </div>

#     </div>
#     <!-- COLLECTED JS -->
        
        
#     <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css">
#     <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/movie/4aca95d66d37ec0712b3d19973b5d8feb75f2f05/css/movie/mod/reg_login_pop.css">
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/2c0c1c6b83f9a457b0f38c38a32fc43a42ec9bad/js/do.js" data-cfg-autoload="false"></script>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js"></script>
#     <script type="text/javascript">
#         var HTTPS_DB='https://www.douban.com';
# var account_pop={open:function(o,e){e?referrer="?referrer="+encodeURIComponent(e):referrer="?referrer="+window.location.href;var n="",i="",t=448;n="用户登录",i="https://accounts.douban.com/passport/login_popup?source=movie";var r=document.location.protocol+"//"+document.location.hostname,a=dui.Dialog({width:340,title:n,height:t,cls:"account_pop",isHideTitle:!0,modal:!0,content:"<iframe scrolling='no' frameborder='0' width='340' height='"+t+"' src='"+i+"' name='"+r+"'></iframe>"},!0),c=a.node;if(c.undelegate(),c.delegate(".dui-dialog-close","click",function(){var o=$("body");o.find("#login_msk").hide(),o.find(".account_pop").remove()}),$(window).width()<478){var d="";"reg"===o?d=HTTPS_DB+"/accounts/register"+referrer:"login"===o&&(d=HTTPS_DB+"/accounts/login"+referrer),window.location.href=d}else a.open();$(window).bind("message",function(o){"https://accounts.douban.com"===o.originalEvent.origin&&(c.find("iframe").css("height",o.originalEvent.data),c.height(o.originalEvent.data),a.update())})}};Douban&&Douban.init_show_login&&(Douban.init_show_login=function(o){var e=$(o);e.click(function(){var o=e.data("ref")||"";return account_pop.open("login",o),!1})}),Do(function(){$("body").delegate(".pop_register","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("reg",e),!1}),$("body").delegate(".pop_login","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("login",e),!1})});
#     </script>

    
    




    
# <script type="text/javascript">
#     (function (global) {
#         var newNode = global.document.createElement('script'),
#             existingNode = global.document.getElementsByTagName('script')[0],
#             adSource = '//erebor.douban.com/',
#             userId = '',
#             browserId = 'oi6GMJ3oAuw',
#             criteria = '3:/top250',
#             preview = '',
#             debug = false,
#             adSlots = ['dale_movie_top250_bottom_right'];

#         global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
#         global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

#         newNode.setAttribute('type', 'text/javascript');
#         newNode.setAttribute('src', '//img1.doubanio.com/YWVrMm1iYy9mL2FkanMvN2ZmNmEyM2M0ZDNjMmQxYWVkMjMwZDIwMDU5NWI2YTFkNDc5YjExYi9hZC5yZWxlYXNlLmpz');
#         newNode.setAttribute('async', true);
#         existingNode.parentNode.insertBefore(newNode, existingNode);
#     })(this);
# </script>











    
  









# <script type="text/javascript">
# var _paq = _paq || [];
# _paq.push(['trackPageView']);
# _paq.push(['enableLinkTracking']);
# (function() {
#     var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
#     _paq.push(['setTrackerUrl', u+'piwik']);
#     _paq.push(['setSiteId', '100001']);
#     var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
#     g.type='text/javascript';
#     g.defer=true;
#     g.async=true;
#     g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
#     s.parentNode.insertBefore(g,s);
# })();
# </script>

# <script type="text/javascript">
# var setMethodWithNs = function(namespace) {
#   var ns = namespace ? namespace + '.' : ''
#     , fn = function(string) {
#         if(!ns) {return string}
#         return ns + string
#       }
#   return fn
# }

# var gaWithNamespace = function(fn, namespace) {
#   var method = setMethodWithNs(namespace)
#   fn.call(this, method)
# }

# var _gaq = _gaq || []
#   , accounts = [
#       { id: 'UA-7019765-1', namespace: 'douban' }
#     , { id: 'UA-7019765-19', namespace: '' }
#     ]
#   , gaInit = function(account) {
#       gaWithNamespace(function(method) {
#         gaInitFn.call(this, method, account)
#       }, account.namespace)
#     }
#   , gaInitFn = function(method, account) {
#       _gaq.push([method('_setAccount'), account.id]);
#       _gaq.push([method('_setSampleRate'), '5']);

      
#   _gaq.push([method('_addOrganic'), 'google', 'q'])
#   _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
#   _gaq.push([method('_addOrganic'), 'soso', 'w'])
#   _gaq.push([method('_addOrganic'), 'youdao', 'q'])
#   _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
#   _gaq.push([method('_addOrganic'), 'sogou', 'query'])
#   if (account.namespace) {
#     _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
#     _gaq.push([method('_addIgnoredOrganic'), 'douban'])
#     _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
#     _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
#   }

#       if (account.namespace === 'douban') {
#         _gaq.push([method('_setDomainName'), '.douban.com'])
#       }

#         _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

#         _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);

#       _gaq.push([method('_trackPageview')])
#     }

# for(var i = 0, l = accounts.length; i < l; i++) {
#   var account = accounts[i]
#   gaInit(account)
# }


# ;(function() {
#     var ga = document.createElement('script');
#     ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
#     ga.setAttribute('async', 'true');
#     document.documentElement.firstChild.appendChild(ga);
# })()
# </script>








      

#     <!-- dae-web-movie--default-86c8b8b5f7-w8zc8-->

#   <script>_SPLITTEST=''</script>





# <div id="search_suggest" style="display: none; top: 78px; left: 174.406px;"><ul></ul></div><ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;" data-ad-status="unfilled"><ins id="aswift_1_expand" style="display:inline-table;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_1_anchor" style="display:block;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;"><iframe id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-4830389020085397&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;lmt=1627788578&amp;plat=9%3A32776%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1081344%2C32%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fmovie.douban.com%2Ftop250&amp;ea=0&amp;flash=0&amp;pra=7&amp;wgl=1&amp;uach=WyJtYWNPUyIsIjEwXzE1XzciLCJ4ODYiLCIiLCI5Mi4wLjQ1MTUuMTA3IixbXSxudWxsLG51bGwsbnVsbF0.&amp;tt_state=W3siaXNzdWVyT3JpZ2luIjoiaHR0cHM6Ly9hdHRlc3RhdGlvbi5hbmRyb2lkLmNvbSIsInN0YXRlIjo3fV0.&amp;dt=1627788578609&amp;bpp=3&amp;bdt=1805&amp;idt=113&amp;shv=r20210728&amp;mjsv=m202107290101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3D10f2af77a1ea3866-220684e835c60045%3AT%3D1614740879%3ART%3D1614740879%3AS%3DALNI_MYfycbmdCJOTfOnNxwELjLoRpefYQ&amp;prev_fmts=300x250&amp;nras=1&amp;correlator=2048992231746&amp;frm=20&amp;pv=1&amp;ga_vid=1219040786.1616633654&amp;ga_sid=1627788578&amp;ga_hid=38252945&amp;ga_fc=1&amp;u_tz=480&amp;u_his=5&amp;u_java=0&amp;u_h=1120&amp;u_w=1792&amp;u_ah=1011&amp;u_aw=1792&amp;u_cd=30&amp;u_nplug=3&amp;u_nmime=4&amp;adx=-12245933&amp;ady=-12245933&amp;biw=1777&amp;bih=932&amp;scr_x=0&amp;scr_y=0&amp;eid=20211866%2C21065725%2C21067496&amp;oid=3&amp;pvsid=407474137959711&amp;pem=875&amp;eae=2&amp;fc=896&amp;brdim=0%2C109%2C0%2C109%2C1792%2C25%2C1792%2C1011%2C1792%2C932&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=32768&amp;bc=31&amp;ifi=2&amp;uci=a!2&amp;fsb=1&amp;dtd=122" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!2" data-load-complete="true"></iframe></ins></ins></ins><iframe id="google_osd_static_frame_8769178137431" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;"></iframe><iframe src="https://www.google.com/recaptcha/api2/aframe" width="0" height="0" style="display: none;"></iframe></body>
