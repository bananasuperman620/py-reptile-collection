from core import get_play_link, query_id
from flask import Flask ,render_template, request


# 登录后的cookie才能查看vip电影
# P00001 或者 p00007
cookie = 'P00001=_1m3LzZu7QFhYqTUry1cLRFCt0bZzbtK5DsN5nk6K8JOfm20E1HI5j82tHouaaQiOntX0c;'

# 这个从cookie中的QY00001获取，好像是用户id
uid = '_101874118'


app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url', '')
    tvid, vid = query_id(url)
    script, k_uid = get_play_link(tvid, vid, uid, cookie)

    return render_template('player.html', tvid=tvid, vid=vid, k_uid=k_uid, uid=uid, script=script)



app.run('0.0.0.0', port=80)

