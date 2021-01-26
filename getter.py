"""
这是获取免费代理的模块
"""
"""
目标网址：
快代理：https://www.kuaidaili.com/free/
云代理：http://www.ip3366.net/
89代理：https://www.89ip.cn/
"""

import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

re_pattern = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)


def spider_kuai_proxy():
    """抓取快代理的ip地址和端口号"""
    for page in range(1, 6):
        html_data = requests.get(url=f'http://www.ip3366.net/?stype=1&page={page}', headers=headers).text
        print('快代理:', f'http://www.ip3366.net/?stype=1&page={page}')
        ip = re.findall(re_pattern, html_data)
        # print(ip)
        # 将ip从列表中的元组中都提取出来
        for ip, port in ip:
            yield ip + ':' + port


def spider_yun_proxy():
    """抓取云代理的ip地址和端口号"""
    for page in range(1, 6):
        html_data = requests.get(url=f'http://www.ip3366.net/?stype=1&page={page}', headers=headers).text
        print('云代理:', f'http://www.ip3366.net/?stype=1&page={page}')
        ip = re.findall(re_pattern, html_data)
        # print(ip)
        # 将ip从列表中的元组中都提取出来
        for ip, port in ip:
            yield ip + ':' + port


def spider_89_proxy():
    """抓取89代理的ip地址和端口号"""
    for page in range(1, 6):
        html_data = requests.get(url=f'https://www.89ip.cn/index_{page}.html', headers=headers).text
        print('89代理:', f'https://www.89ip.cn/index_{page}.html')
        ip = re.findall(re_pattern, html_data)
        # print(ip)
        # 将ip从列表中的元组中都提取出来
        for ip, port in ip:
            yield ip + ':' + port


# for i in spider_kuai_proxy():
#     print(i)
# for i in spider_yun_proxy():
#     print(i)
# for i in spider_89_proxy():
#     print(i)

"""
让所有函数对象，依次去运行
🦆鸭子🦆类型
不关心对象是什么类型，只关注对象的行为。
在这里，不关注函数名称是什么类型，即不管它是不是函数，我只关注，加了括号之后，它能够运行
"""
get_proxy_func_list = [spider_kuai_proxy, spider_yun_proxy, spider_89_proxy]
# if __name__ == '__main__':
#     get_proxy_func_list = [spider_kuai_proxy, spider_yun_proxy, spider_89_proxy]
# for func in get_proxy_func_list:
#     proxies = func()
#     for proxy in proxies:
#         print(proxy)
# redis_client = RedisClient()
# redis_client.add(proxy)
