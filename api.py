"""这是服务模块，用于向爬虫的py文件提供获取代理ip的接口，利用flask共建一个网站，里面存放了代理的ip地址"""

import flask
from db import RedisClient
from flask import request
from flask import jsonify

# 实例化一个app对象
app = flask.Flask(__name__)

# 创建一个数据库模块的对象
client = RedisClient()


# 构建视图函数
@app.route('/')  # 根目录
def index():
    """注意：视图函数，只能返回字符串"""
    return '欢迎来到代理池'


@app.route('/get')
# 这个视图随机返回一个代理，这个代理同db模块中的random模块，优先返回分支较高的代理
def get_proxy():
    one_proxy = client.random()
    return one_proxy


@app.route('/getcount')
# 获取指定数量的代理，数量根据查询参数指定
def get_any_proxy():
    num = request.args.get('num', '')  # 这里有可能用户忘记传入查询参数，如果用户忘记传入了查询参数的话，默认返回一个proxy值
    # 做判断
    if not num:
        num = 1
    else:
        num = int(num)

    any_proxy = client.count_for_num(num)

    # 返回指定数量的代理，这里返回的是列表，要在flask中进行反序列化
    return jsonify(any_proxy)


@app.route('/getnum')
# 获取所有代理的数量
def get_count_proxy():
    count = client.count()
    return jsonify(count)


@app.route('/getall')
# 获取所有代理
def get_all_proxy():
    all_proxy = client.all()
    return jsonify(all_proxy)


if __name__ == '__main__':
    app.run()
