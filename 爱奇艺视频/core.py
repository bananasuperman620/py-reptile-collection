import hashlib
import json
import time
from urllib.parse import urlencode
from urllib.request import quote

import requests
from pyquery import PyQuery as PQ


def cmd5x(text):
    url = 'http://localhost:8888/cmd5x'
    req = requests.post(url, data=dict(query_args=text))
    return req.text

def get_time():
    url = 'http://localhost:8888/get_time'
    req = requests.post(url)
    return req.text

def get_authKey():
    url = 'http://localhost:8888/get_authKey'
    req = requests.post(url)
    return req.text

def get_qc005():
    url = 'http://localhost:8888/get_qc005'
    req = requests.post(url)
    return req.text


def query_id(url):
    req = requests.get(url)
    pq = PQ(req.text)
    tvid = pq('*[data-player-tvid]').attr('data-player-tvid')
    vid = pq('*[data-player-videoid]').attr('data-player-videoid')
    # tvid = '731596400'
    # vid = '91fd365a82dc445086286610dd0528d0'
    return tvid, vid


def get_play_link(tvid, vid, uid, cookie):
    # 打包

    tm = get_time()
    k_uid = get_qc005()
    authKey = get_authKey()

    # tm = int(time.time()) * 1000
    # k_uid = 'd521f8d24d92ab5611c71925ab267185'
    # authKey = '371edcdae1bc61d8c86d59ecef8f3866'
    query = dict(
        tvid=tvid,
        bid=800,
        vid=vid,
        src='01010031010000000000',
        vt=0,
        rs=1,
        uid=uid,
        ori='pcw',
        ps=0,
        tm=tm,
        qd_v=1,
        k_uid=k_uid, # 随机的
        pt=0,
        d=0,
        s='',
        lid='',
        cf='',
        ct='',
        authKey=authKey, # 随机的
        k_tag=1,
        ppt=0,
        dfp='',
        locale='zh_cn',
        prio=quote('{"ff":"flv", "code":"2"}'),
        pck='',
        k_err_retries=0,
        ut=1,
        bop=quote('{"version":"7.0","dfp":""}'),
        callback='Qc556570ac81f604e78ccdf9b78a21a02',
    )
    
    query_url = '/jp/dash?' + urlencode(query)    
    vf = cmd5x(query_url)
    query_url += '&vf=' + vf


    # 查询播放链接
    url = 'http://cache.video.iqiyi.com' + query_url

    headers = {
        'cookie': cookie
    }
    content = requests.get(url, headers=headers).text
    return content, k_uid
