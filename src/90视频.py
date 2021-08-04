
# 00
# https://www.pearvideo.com/video_1737650


# xhr
# https://www.pearvideo.com/videoStatus.jsp?contId=1737650&mrd=0.6301524948979604

# 404
# https://video.pearvideo.com/mp4/adshort/20210804/1628063935756-15737939_adpkg-ad_hd.mp4

# good
# https://video.pearvideo.com/mp4/adshort/20210804/cont-1737650-15737939_adpkg-ad_hd.mp4

import requests

url = 'https://www.pearvideo.com/video_1737650'

contId = url.split('_')[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.6301524948979604"

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
#    防盗链: 溯源 本次请求上一级页面是什么
   'Referer': 'https://www.pearvideo.com/video_1737650'
}

res = requests.get(videoStatusUrl, headers=headers)

resJson = res.json()

vSrc = resJson['videoInfo']['videos']['srcUrl']
systemTime = resJson['systemTime']

vCSrc = vSrc.replace(systemTime, f'cont-{contId}')

vName = vSrc.split('/')[-1]


# 下载视频
with open(vName, mode='wb') as f:
    vShow = requests.get(vCSrc)
    f.write(vShow.content)
    vShow.close()
    f.close()

res.close()










