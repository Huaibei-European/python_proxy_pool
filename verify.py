"""
这是检测模块，检测代理的ip是否可用

多线程检测
"""

import requests
from db import RedisClient
import concurrent.futures
import datetime
import time
from config import TEST_URL


# 实例化redis数据库对象
client = RedisClient()


def verify_proxy(proxy):
    """这个函数用于检测传如的代理ip是否可用"""

    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        response = requests.get(url=TEST_URL, proxies=proxies, timeout=2)
        if response.status_code in [200, 206, 208, 302]:
            print('当前代理可用，将其设置为100分', proxy)
            client.max(proxy)  # 将传入的检测的可用的代理设置为100分

        else:
            print('请求的代理状态码不可用，执行降分操作', proxy)
            client.decrease(proxy)
    except Exception as e:
        print('请求超时，代理不可用，执行降分操作', proxy)
        client.decrease(proxy)


"""以上定义了一个检测模块，一次传进去一个代理，但检测的速度太慢，使用多线程检测"""


def verify_thread_pool():
    """使用线程池测试代理"""
    print('正在检测代理')
    # 首先从数据库中查询到所有的额代理，然后再传入到检测模块中
    proxy_list = client.all()
    # 用线程池去检测代理，遍历列表，提交proxy，提交任务
    for proxy in proxy_list:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            executor.submit(verify_proxy, proxy)


if __name__ == '__main__':
    verify_thread_pool()
