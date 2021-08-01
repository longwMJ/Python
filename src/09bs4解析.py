text = """
				<body>
  <!-- Banner-->
  <nav class="navbar navbar-default navbar-fixed-top">
    <div class="container">
      <!--小屏幕导航按钮和logo-->
      <div class="navbar-header">
        <img
          src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/logo.png"
          style="margin-top: 20px"
          class="img-responsive"
          alt="logo"
        />
      </div>
      <!--小屏幕导航按钮和logo-->
      <!--导航-->
      <div class="navbar-collapse collapse">
        <ul class="nav navbar-nav navbar-right">
          <li>
            <a href="./index.html" class="navactive scroll header-avtive"
              >首页</a
            >
          </li>
          <li><a href="./companyProfile.html" class="">公司简介</a></li>
          <li><a href="./newsCenter.html" class=""> 新闻中心</a></li>
          <li>
            <a
              href="./msgCenter"
              id="msgCenter"
              class="dropdown-toggle"
              data-toggle="dropdown"
              role="button"
              aria-haspopup="true"
              aria-expanded="false"
              ><span data-letters="Pages">信息中心</span
              ><span class="caret"></span
            ></a>
            <ul class="nav dropdown-menu">
              <li><a href="./priceDetail.html" class="">价格行情</a></li>
              <li><a href="./informationCenter.html" class="">行情分析</a></li>
            </ul>
          </li>
          <li><a href="./merchantCenter.html" class="">商户中心</a></li>
          <li><a href="./productCenter.html" class="">产品中心</a></li>
        </ul>
      </div>
      <!--导航-->
    </div>
    <script>
      $(document).ready(function () {
                var price;
      	$(".nav li a").each(function () {
      		var $this = $(this);
      		var&nbsp;location=window.location.href;
      		var&nbsp;s=location.indexOf("?");
      		var type = "";
      		if(s>=0){
                        type = location.substring(s,location.length);
      		&nbsp;&nbsp;&nbsp;&nbsp;location=location.substring(0,s);
      		} &nbsp;&nbsp;
      		// if ($this[0].href == String(location)) {
      		// 	$this.addClass("header-avtive");
      		// }else{
      		// 	$this.removeClass("header-avtive");
      		// } &nbsp;&nbsp;

      		if ($this[0].href == String(location) || ($this[0].href.indexOf('newsCenter.html') > 0 && String(location).indexOf("news-") > 0)
      			|| ($this[0].href.indexOf('informationCenter.html') > 0 && String(location).indexOf("infor-") > 0)) {
      		    if (String(location).indexOf("priceDetail.html") > 0
      				|| String(location).indexOf("informationCenter.html") > 0
      				|| String(location).indexOf("infor-") > 0) {
                            $("#msgCenter").addClass("navactive scroll header-avtive");
      			} else {
                            $this.addClass("navactive scroll header-avtive");
      			}
      		}else{
      			$this.removeClass("navactive scroll header-avtive");
      		}

      	});


      });
    </script>
  </nav>

  <!-- banner -->
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1" class=""></li>
      <li data-target="#myCarousel" data-slide-to="2" class=""></li>
    </ol>
    <div class="carousel-inner" role="listbox" style="margin-top: 72px">
      <a href=""> </a>
      <div class="item next left">
        <a href=""> </a>
        <div class="container1">
          <a href="">
            <img
              class="imgs"
              src="http://newlands-web.oss-cn-beijing.aliyuncs.com/banner/images/ebb7f369-8f35-44bf-b4e1-df3e14429104.jpg"
              alt=""
              style="height: 700px; width: 100%"
            />
          </a>
          <div class="carousel-caption">
            <a href="">
              <h3></h3>
              <p></p>
            </a>
            <div class="agileits-button top_ban_agile">
              <a href=""> </a
              ><a
                class="btn btn-lg"
                href="#"
                data-toggle="modal"
                data-target="#myModal"
              ></a>
            </div>
          </div>
        </div>
      </div>
      <a href="http://www.xinfadi.com.cn/news-48.html"> </a>
      <div class="item item2">
        <a href="http://www.xinfadi.com.cn/news-48.html"> </a>
        <div class="container2">
          <a href="http://www.xinfadi.com.cn/news-48.html">
            <img
              class="imgs"
              src="http://newlands-web.oss-cn-beijing.aliyuncs.com/banner/images/0690c769-f8ad-4de0-b8f3-22dc8fe37174.jpg"
              alt=""
              style="height: 700px; width: 100%"
            />
          </a>
          <div class="carousel-caption">
            <a href="http://www.xinfadi.com.cn/news-48.html">
              <h3></h3>
              <p></p>
            </a>
            <div class="agileits-button top_ban_agile">
              <a href="http://www.xinfadi.com.cn/news-48.html"> </a
              ><a
                class="btn btn-lg"
                href="#"
                data-toggle="modal"
                data-target="#myModal"
              ></a>
            </div>
          </div>
        </div>
      </div>
      <a href=""> </a>
      <div class="item item3 active left">
        <a href=""> </a>
        <div class="container3">
          <a href="">
            <img
              class="imgs"
              src="http://newlands-web.oss-cn-beijing.aliyuncs.com/banner/images/2d672c23-f7e2-437b-b836-960bc847495c.jpg"
              alt=""
              style="height: 700px; width: 100%"
            />
          </a>
          <div class="carousel-caption">
            <a href="">
              <h3></h3>
              <p></p>
            </a>
            <div class="agileits-button top_ban_agile">
              <a href=""> </a
              ><a
                class="btn btn-lg"
                href="#"
                data-toggle="modal"
                data-target="#myModal"
              ></a>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
  <!-- About Us-->
  <div class="about" style="padding-top: 20px; padding-bottom: 20px">
    <div class="container" style="width: 1170px">
      <b style="color: red"
        >公告：各位用户大家好，新版网站上线测试中，如您发现网站问题以及有好的修改建议，请及时告知我们，谢谢！QQ：8035129</b
      >
    </div>
  </div>

  <div class="about" id="about">
    <div class="container new" style="width: 1170px">
      <h3>每日价格行情</h3>
      <h5>Daily price quotation</h5>
      <!-- 列表标题 -->
      <ul id="ul">
        <li class="ul_li" id="1186">
          <div>蔬菜</div>
          <div></div>
        </li>
        <li id="1187">
          <div>水果</div>
          <div></div>
        </li>
        <li id="1189">
          <div>肉禽蛋</div>
          <div></div>
        </li>
        <li id="1190">
          <div>水产</div>
          <div></div>
        </li>
        <li id="1188">
          <div>粮油</div>
          <div></div>
        </li>
        <li id="1203">
          <div>豆制品</div>
          <div></div>
        </li>
        <li id="1204">
          <div>调料</div>
          <div></div>
        </li>
      </ul>

      <a href="./priceDetail.html"
        ><img
          class="ckgdImg"
          src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/ckgd.png"
          alt=""
      /></a>
      <div id="div">
        <!-- 4 -->
        <!--<div th:class="${catStat.count==1?'div_div':''}"   th:each="cat:${catlist}">-->
        <div class="div_div">
          <div class="tablebox">
            <div class="tbl-header">
              <table border="0" cellspacing="0" cellpadding="0">
                <thead>
                  <tr>
                    <th width="140px">品名</th>
                    <th width="140px">最低价</th>
                    <th width="140px">平均价</th>
                    <th width="140px">最高价</th>
                    <th width="140px">规格</th>
                    <th width="140px">产地</th>
                    <th width="140px">单位</th>
                    <th>发布日期</th>
                  </tr>
                </thead>
                <tbody style="opacity: 0"></tbody>
              </table>
            </div>
            <div class="tbl-body">
              <table border="0" cellspacing="0" cellpadding="0">
                <thead>
                  <tr>
                    <th width="140px">品名</th>
                    <th width="140px">最低价</th>
                    <th width="140px">平均价</th>
                    <th width="140px">最高价</th>
                    <th width="140px">规格</th>
                    <th width="140px">产地</th>
                    <th width="140px">单位</th>
                    <th>发布日期</th>
                  </tr>
                </thead>
                <tbody id="ulTableBody" class="ul">
                  
                  <tr>
                    <td>大白菜</td>
                    <td>0.8</td>
                    <td>0.9</td>
                    <td>1.0</td>
                    <td></td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>娃娃菜</td>
                    <td>0.8</td>
                    <td>1.0</td>
                    <td>1.2</td>
                    <td>大</td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>小白菜</td>
                    <td>1.6</td>
                    <td>1.8</td>
                    <td>2.0</td>
                    <td></td>
                    <td></td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>芹菜</td>
                    <td>1.2</td>
                    <td>1.35</td>
                    <td>1.5</td>
                    <td></td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>西芹</td>
                    <td>1.5</td>
                    <td>1.75</td>
                    <td>2.0</td>
                    <td></td>
                    <td></td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>菠菜</td>
                    <td>2.0</td>
                    <td>2.75</td>
                    <td>3.5</td>
                    <td>普通\精选</td>
                    <td>蒙</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>莴笋</td>
                    <td>1.0</td>
                    <td>1.25</td>
                    <td>1.5</td>
                    <td>毛\净</td>
                    <td></td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>团生菜</td>
                    <td>1.2</td>
                    <td>1.5</td>
                    <td>1.8</td>
                    <td>毛\净</td>
                    <td></td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>圆白菜</td>
                    <td>0.5</td>
                    <td>0.7</td>
                    <td>0.9</td>
                    <td>实\暄</td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>紫甘蓝</td>
                    <td>0.6</td>
                    <td>0.65</td>
                    <td>0.7</td>
                    <td>精选</td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>散叶生菜</td>
                    <td>2.5</td>
                    <td>2.75</td>
                    <td>3.0</td>
                    <td>毛\净</td>
                    <td>京冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>油菜</td>
                    <td>2.0</td>
                    <td>2.25</td>
                    <td>2.5</td>
                    <td></td>
                    <td>京</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>香菜</td>
                    <td>4.0</td>
                    <td>5.0</td>
                    <td>6.0</td>
                    <td></td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>茴香</td>
                    <td>4.0</td>
                    <td>4.5</td>
                    <td>5.0</td>
                    <td></td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>韭菜</td>
                    <td>1.5</td>
                    <td>1.75</td>
                    <td>2.0</td>
                    <td></td>
                    <td>晋</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>韭菜苔</td>
                    <td>2.5</td>
                    <td>2.75</td>
                    <td>3.0</td>
                    <td></td>
                    <td></td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>苦菊</td>
                    <td>3.0</td>
                    <td>3.5</td>
                    <td>4.0</td>
                    <td></td>
                    <td>辽</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>油麦菜</td>
                    <td>3.0</td>
                    <td>3.5</td>
                    <td>4.0</td>
                    <td></td>
                    <td>京</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>散菜花</td>
                    <td>2.4</td>
                    <td>2.7</td>
                    <td>3.0</td>
                    <td>精选</td>
                    <td>豫\苏</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>绿菜花</td>
                    <td>2.0</td>
                    <td>2.25</td>
                    <td>2.5</td>
                    <td></td>
                    <td>京冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>绿豆芽</td>
                    <td>0.95</td>
                    <td>0.98</td>
                    <td>1.0</td>
                    <td></td>
                    <td></td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>黄豆芽</td>
                    <td>0.85</td>
                    <td>0.88</td>
                    <td>0.9</td>
                    <td></td>
                    <td></td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>番茄</td>
                    <td>1.1</td>
                    <td>1.3</td>
                    <td>1.5</td>
                    <td>黑框</td>
                    <td>冀鲁蒙</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>番茄</td>
                    <td>1.3</td>
                    <td>1.55</td>
                    <td>1.8</td>
                    <td>白框</td>
                    <td>冀鲁</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>樱西</td>
                    <td>2.4</td>
                    <td>2.6</td>
                    <td>2.8</td>
                    <td>小红</td>
                    <td></td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>黄瓜</td>
                    <td>1.5</td>
                    <td>2.0</td>
                    <td>2.5</td>
                    <td>袋\箱</td>
                    <td>蒙辽</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>黄瓜</td>
                    <td>2.5</td>
                    <td>2.85</td>
                    <td>3.2</td>
                    <td>鲜干花</td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>小黄瓜</td>
                    <td>3.5</td>
                    <td>4.0</td>
                    <td>4.5</td>
                    <td>旱黄瓜</td>
                    <td>辽</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>茄子</td>
                    <td>1.5</td>
                    <td>2.25</td>
                    <td>3.0</td>
                    <td>精选</td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>长茄</td>
                    <td>1.5</td>
                    <td>1.85</td>
                    <td>2.2</td>
                    <td>精选</td>
                    <td>冀\晋</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>广茄</td>
                    <td>1.5</td>
                    <td>2.25</td>
                    <td>3.0</td>
                    <td></td>
                    <td></td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>线茄</td>
                    <td>2.0</td>
                    <td>2.5</td>
                    <td>3.0</td>
                    <td>精选</td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>冬瓜</td>
                    <td>0.35</td>
                    <td>0.43</td>
                    <td>0.5</td>
                    <td>吊</td>
                    <td>冀辽</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>冬瓜</td>
                    <td>0.25</td>
                    <td>0.3</td>
                    <td>0.35</td>
                    <td>地</td>
                    <td>冀辽</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>小毛冬瓜</td>
                    <td>0.6</td>
                    <td>0.8</td>
                    <td>1.0</td>
                    <td>长</td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>架豆</td>
                    <td>3.5</td>
                    <td>4.5</td>
                    <td>5.5</td>
                    <td></td>
                    <td>冀晋</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>豆王</td>
                    <td>3.5</td>
                    <td>4.5</td>
                    <td>5.5</td>
                    <td>精选</td>
                    <td>晋甘</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>扁豆</td>
                    <td>4.0</td>
                    <td>4.5</td>
                    <td>5.0</td>
                    <td>精选</td>
                    <td>冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>豇豆</td>
                    <td>2.5</td>
                    <td>3.25</td>
                    <td>4.0</td>
                    <td></td>
                    <td>冀鲁京</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                  <tr>
                    <td>白不老</td>
                    <td>4.0</td>
                    <td>4.5</td>
                    <td>5.0</td>
                    <td></td>
                    <td>辽冀</td>
                    <td>斤</td>
                    <td>2021-08-01</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- News-->
  <div class="news" id="news">
    <div class="container" style="width: 1170px">
      <h3>市场行情分析</h3>
      <h5>Market analysis</h5>
      <div class="schqLeftDiv col-md-3">
        <img src="./img/hangqing.png" class="img-responsive1" alt="" />
      </div>
      <div
        class="quotation col-md-8"
        style="height: auto !important; margin-bottom: 15px"
      >
        <div style="margin-bottom: 15px">
          <div class="news-title" style="margin-bottom: 1px">
            <div>每周市场动态（2021.7.17-2021.7.23）</div>
            <div class="news-title-right">
              <a href="/news-51.html"
                ><img
                  src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/index/other.png"
                  alt=""
              /></a>
            </div>
          </div>
          <span
            >一、白条猪价格走势本周，白条猪批发的平均价继续进行调整，波动的幅度较大，价格在波动中有所上涨。7月2...</span
          >
        </div>
        <div style="margin-bottom: 15px">
          <div class="news-title" style="margin-bottom: 1px">
            <div>每周市场动态（2021.7.10-2021.7.16）</div>
            <div class="news-title-right">
              <a href="/news-52.html"
                ><img
                  src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/index/other.png"
                  alt=""
              /></a>
            </div>
          </div>
          <span
            >一、白条猪价格走势本周，白条猪批发的平均价进入调整阶段，价格不时地出现一些波动，并且在波动中下行。7...</span
          >
        </div>
        <div style="margin-bottom: 15px">
          <div class="news-title" style="margin-bottom: 1px">
            <div>每周市场动态（2021.7.3-2021.7.9）</div>
            <div class="news-title-right">
              <a href="/news-47.html"
                ><img
                  src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/index/other.png"
                  alt=""
              /></a>
            </div>
          </div>
          <span
            >一、白条猪价格走势本周前期，白条猪批发的平均价缓慢下行，周后期出现反弹。7月9日，新发地市场白条猪批...</span
          >
        </div>
      </div>

      <div style="text-align: center; margin-top: 10px">
        <a href="./informationCenter.html"
          ><img
            src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/index/other.png"
            style="width: 160px"
            alt=""
        /></a>
      </div>
    </div>
  </div>

  <!--/News-->
  <div id="bbs2" class="about" style="padding: 0 0 50px 0">
    <div class="container" style="width: 60%">
      <h3>新闻中心</h3>
      <h5>Market analysis</h5>
      <!--<div class="newsList col-md-12 newsSelected">-->
      <!--<div class="col-md-4 news" th:each="news:${newslist}">-->
      <!--<a href="#">-->
      <!--<img th:src="${news.pictureUrl}"  class="img-responsive">-->
      <!--</a>-->
      <!--<span class="newsTime"><b  th:text="${news.title}">标题1</b></span></br>-->
      <!--<a href="#" class="newsTitle"><span th:text="${news.introduction}"></span></a>-->
      <!--</div>-->
      <!--</div>-->

      <div
        class="
          swiper-container
          swiper-container-initialized
          swiper-container-horizontal
          swiper-container-pointer-events
        "
      >
        <div
          class="swiper-wrapper"
          id="swiper-wrapper-50029812996cc399"
          aria-live="polite"
          style="transform: translate3d(0px, 0px, 0px)"
        >
          <div
            class="swiper-slide news swiper-slide-active"
            role="group"
            aria-label="1 / 5"
            style="width: 228.667px"
          >
            <a href="/news-56.html">
              <img
                src="http://newlands-n.oss-cn-beijing.aliyuncs.com/IMAGE/bcb0e4ec-110c-4679-ae15-e4db4b9be403.jpg"
                class="img-responsive"
              />
            </a>
            <span class="newsTime"
              ><b>张玉玺董事长率队到蒙阴县进行农业考察</b></span
            ><br />
            <a href="/news-56.html" class="newsTitle"
              ><span
                >7月25日，以“喜庆建党百年·共赴仙桃盛会”为主题的蒙阴县第四届蟠桃文化节隆重开幕，新发地市场董事长...</span
              ></a
            >
          </div>
          <div
            class="swiper-slide news swiper-slide-next"
            role="group"
            aria-label="2 / 5"
            style="width: 228.667px"
          >
            <a href="/news-53.html">
              <img
                src="http://newlands-n.oss-cn-beijing.aliyuncs.com/IMAGE/1a11d06d-3a17-4bda-beef-da45c0df9eea.jpg"
                class="img-responsive"
              />
            </a>
            <span class="newsTime"
              ><b>【最新动态】新发地市场向新乡等受灾地区捐赠物资</b></span
            ><br />
            <a href="/news-53.html" class="newsTitle"
              ><span
                >近日，河南郑州、新乡等地因暴雨侵袭受灾严重，河南人民正经受着一场重大的考验，很多地方断水断电，生活基...</span
              ></a
            >
          </div>
          <div
            class="swiper-slide news"
            role="group"
            aria-label="3 / 5"
            style="width: 228.667px"
          >
            <a href="/news-50.html">
              <img
                src="http://newlands-n.oss-cn-beijing.aliyuncs.com/IMAGE/84d6bd32-b1fa-46c5-aa06-af50fea0d420.jpg"
                class="img-responsive"
              />
            </a>
            <span class="newsTime"
              ><b>江西省政府副省长胡强莅临新发地视察调研考察</b></span
            ><br />
            <a href="/news-50.html" class="newsTitle"
              ><span
                >7月23日上午，江西省政府副省长胡强、省农业厅副厅长邓贤贵一行莅临新发地市场，就江西特色农产品在京销...</span
              ></a
            >
          </div>
          <div
            class="swiper-slide news"
            role="group"
            aria-label="4 / 5"
            style="width: 228.667px"
          >
            <a href="/news-49.html">
              <img
                src="http://newlands-n.oss-cn-beijing.aliyuncs.com/IMAGE/b6ab48ae-7216-4b19-bd30-ffee7e39011e.jpg"
                class="img-responsive"
              />
            </a>
            <span class="newsTime"
              ><b>新发地市场木瓜品质升级，价格稳步攀升</b></span
            ><br />
            <a href="/news-49.html" class="newsTitle"
              ><span
                >现在这个季节原本属于木瓜产品消费的淡季，上市量、销售价格理应走低。但是今年情况却有点特殊，因为新发地...</span
              ></a
            >
          </div>
          <div
            class="swiper-slide news"
            role="group"
            aria-label="5 / 5"
            style="width: 228.667px"
          >
            <a href="/news-48.html">
              <img
                src="http://newlands-n.oss-cn-beijing.aliyuncs.com/IMAGE/fad88bab-1979-46ff-9500-0cb00121abf1.jpg"
                class="img-responsive"
              />
            </a>
            <span class="newsTime"
              ><b>【重大新闻】新发地新发云线上大平台全面启动</b></span
            ><br />
            <a href="/news-48.html" class="newsTitle"
              ><span
                >7月21日，在新发地举行新发地新发云线上大平台签约仪式，由北京新发地市场与场内广大商户及国内电商大平...</span
              ></a
            >
          </div>
        </div>
        <!-- 如果需要导航按钮 -->
        <div
          class="swiper-button-prev swiper-button-disabled"
          tabindex="-1"
          role="button"
          aria-label="Previous slide"
          aria-controls="swiper-wrapper-50029812996cc399"
          aria-disabled="true"
        ></div>
        <div
          class="swiper-button-next"
          tabindex="0"
          role="button"
          aria-label="Next slide"
          aria-controls="swiper-wrapper-50029812996cc399"
          aria-disabled="false"
        ></div>
        <span
          class="swiper-notification"
          aria-live="assertive"
          aria-atomic="true"
        ></span>
      </div>

      <div style="text-align: center; padding-top: 10px">
        <a href="./newsCenter.html"
          ><img
            src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/index/other.png"
            style="width: 160px"
            alt=""
        /></a>
      </div>
    </div>
  </div>

  <!--&lt;!&ndash;//Clients&ndash;&gt;-->

  <!--<div class="news" style="padding-top: 20px;padding-bottom: 20px;" >-->
  <!--<div class="container" style="width: 1170px;text-align: center;">-->
  <!--<b style="color: red">尊敬的各位网友：为了给大家提供更优质的服务，本网站即将改版，如您有好的建议和解决方案，请与我们联系，期待您的参与。</b>-->
  <!--</div>-->
  <!--</div>-->
  <script>
    $(function () {
      var swiperSlider = new Swiper(".container .swiper-container", {
        direction: "horizontal",
        loop: false,
        speed: 600,
        autoplay: false,
        slidesPerView: 3,
        // prevButton:'.swiper-container .swiper-prev',
        // nextButton:'.swiper-container .swiper-next',
        // 如果需要前进后退按钮
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
        on: {
          click: function () {
            console.log(1111);
          },
        },
      });
      $(".swiper-prev").on("click", function () {
        swiperSlider.slidePrev();
      });
      $(".swiper-next").on("click", function () {
        swiperSlider.slideNext();
      });
    });

    // var mySwiper = new Swiper ('.swiper-container', {
    //     loop: false, // 循环模式选项
    //     slidesPerView : 3,
    //     slidesPerGroup : 3,
    //
    //     // 如果需要分页器
    //     pagination: {
    //         el: '.swiper-pagination',
    //     },
    //
    //     // 如果需要前进后退按钮
    //     navigation: {
    //         nextEl: '.swiper-button-next',
    //         prevEl: '.swiper-button-prev',
    //     },
    //
    //     // 如果需要滚动条
    //     scrollbar: {
    //         el: '.swiper-scrollbar',
    //     },
    // })
  </script>

  <div class="yw-about-footer">
    <div style="display: flex; justify-content: center">
      <div style="float: left">
        <img
          src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/index/code1.jpg"
          style="width: 120px; height: 120px"
          alt=""
        />
        <div class="iteams-text" style="text-align: center">公众号</div>
      </div>
      <div style="float: left; margin-left: 20px">
        <img
          src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/index/code2.jpg"
          style="width: 120px; height: 120px"
          alt=""
        />
        <div class="iteams-text" style="text-align: center">小程序</div>
      </div>
      <div style="float: left; margin-left: 20px">
        <img
          src="https://newlands-web.oss-cn-beijing.aliyuncs.com/images/index/code3.jpg"
          style="width: 120px; height: 120px"
          alt=""
        />
        <div class="iteams-text" style="text-align: center">抖音</div>
      </div>
    </div>
</body>

"""

from bs4 import BeautifulSoup

# print(text)


# 不加'html.parser', 程序回提出警告
page = BeautifulSoup(text, 'html.parser')

# class是关键字, 所以要加_, 作为区别
# data = page.find('div', class_='tbl-body')
data = page.find('div', attrs={
  "class": 'tbl-body'
})
# print(data)

# [1:] 切片, 去除第一份tr数据
trs = data.find_all('tr')[1:]
# trs = data.find_all('tr')
for t in trs:
  # print(0000)
  # print(t)
  # print(2222)



  # tds = t.find_all('td')
  # name = tds[0].text
  # name1 = tds[1].text
  # name2 = tds[2].text
  # name3 = tds[3].text
  # name4 = tds[4].text
  # name5 = tds[5].text
  # name6 = tds[6].text
 
  # print(name, name1, name2, name3, name4, name5, name6)

  tds = t.find_all_next('td')
  name = tds[0]
  name1 = tds[1]
  name2 = tds[2]
  print(name.text, name1, name2)
 