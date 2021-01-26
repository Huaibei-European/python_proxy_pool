"""这是调度模块，用于调度getter.py, api.py, verify.py和db.py的共同协作运行"""
from db import RedisClient
from getter import get_proxy_func_list
import time
from verify import verify_thread_pool
from api import app
import multiprocessing
from config import GETTER_PROXY, VERIFY_PROXY
from config import SERVER_HOST, SERVER_PORT

start_time = time.time()
# 实例化redis数据库对象
client = RedisClient()


# 首先，要获取代理。所以，要先调度获取代理的模块
class Schedule:
    def getter_proxy(self):
        while True:
            for func in get_proxy_func_list:
                proxies = func()
                for proxy in proxies:
                    print('代理已经写入数据库：', proxy)
                    client.add(proxy)
            time.sleep(GETTER_PROXY)  # 规定每5分钟获取一次代理

    def verify_proxy(self):
        while True:
            verify_thread_pool()
            time.sleep(VERIFY_PROXY)  # 规定每10分钟检测一次数据库中的代理

    # 检测完后，让api模块（服务）运行起来
    def api_server(self):
        app.run(host=SERVER_HOST, port=SERVER_PORT)

    # 调用这三个方法一起去执行
    def run(self):
        print('代理池开始运行')
        getter_proxy_process = multiprocessing.Process(target=self.getter_proxy)
        getter_proxy_process.start()

        verify_proxy_process = multiprocessing.Process(target=self.verify_proxy)
        verify_proxy_process.start()

        api_server_process = multiprocessing.Process(target=self.api_server)
        api_server_process.start()


if __name__ == '__main__':
    work = Schedule()
    work.run()
    while True:
        time.sleep(1)
        end_time = time.time()
        print('\r' + str(end_time - start_time)[0:5])
