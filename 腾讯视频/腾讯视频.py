

"""
视频链接: https://v.qq.com/x/cover/lnnijsrcp2djcm5/y0024fopt3c.html

需要参数
url, coverid,，vid，flowid，guid, tm，ckey

视频id
vid=y0024fopt3c
视频集合id
coverid 就是 lnnijsrcp2djcm5
估计随机生成
guid = 239c51bde49d76854be041f1313dc6eb 不清楚试试硬编码
上报BUG参数
flowid=e2f044cda0b6102b78e7cf0da58b6af1_10201  估计是上报错误的
"""

import requests
import time
from urllib.parse import urlencode


url = 'https://vd.l.qq.com/proxyhttp'
data_url = 'https://v.qq.com/x/cover/lnnijsrcp2djcm5/f0024knp7lr.html'
coverid = 'lnnijsrcp2djcm5'
vid = 'f0024knp7lr'
# flowid = 'dc99c1be3f020f44a1587aed8614f057_10201'
# guid = '239c51bde49d76854be041f1313dc6eb'
# ckey = 'd3a190525e23517d287d519eb5c27956'
# coverid = ''
# vid = ''
flowid = ''
guid = ''
tm = str(int(time.time()))
ckey = ''

cookies = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Host': 'vd.l.qq.com',
    'Referer':'https://v.qq.com/x/cover/lnnijsrcp2djcm5/y0024fopt3c.html',
    'Cookie': 'tvfe_boss_uuid=6b57161838371898; '
}

data= '{"buid":"vinfoad","adparam":"pf=in&ad_type=LD%7CKB%7CPVL&pf_ex=pc&url=' + data_url +'&refer=' + data_url + \
    '&ty=web&plugin=1.0.0&v=3.5.52&coverid=' + coverid + '&vid=' + vid + '&pt=&flowid=' + flowid + '&vptag=%7Cvideolist%3Aclick&pu=' + \
    '&chid=0&adaptor=2&dtype=1&live=0&resp_type=json&guid=' + guid + '&req_type=1&platform=10201&tpid=2&rfid=bb966769b3cb5bb9617e7d44487c79a6_1530975003",'+ \
    '"vinfoparam":"charge=0&defaultfmt=auto&otype=ojson&guid=' + guid + '&flowid=' + flowid + '&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.52' +\
    '&refer=' + data_url + '&host=v.qq.com&ehost=' + data_url +'&sphttps=1&tm=1530975150&spwm=4&unid=&vid=' + vid + \
    '&defn=&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&defsrc=1&encryptVer=7.6&cKey=' + ckey + '&fp2p=1"}'
# print(data)
print(requests.post(url, data=data, cookies=cookies).content)    

