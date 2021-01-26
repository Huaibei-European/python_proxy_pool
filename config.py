"""这是配置文件"""
"""数据库配置"""
REDIS_HOST = '127.0.0.1'  # 数据库所在的ip地址
REDIS_PORT = 6379  # 数据库指定端口
REDIS_DATABASE = 0  # 操作哪一个数据库

REDIS_OBJECT = 'PROXIES'  # 有序列表

"""时间间隔配置"""
GETTER_PROXY = 60 * 5  # 获取代理的时间间隔
VERIFY_PROXY = 60 * 10  # 验证代理的时间间隔

"""服务器配置"""
SERVER_HOST = '127.0.0.1'  # API服务的地址
SERVER_PORT = 5000  # API服务的端口

"""测试的地址"""
TEST_URL = 'https://www.baidu.com'  # 测试地址

"""数据库的分数设置"""
INIT_SCORE = 10  # 初始分数
HIGH_SCORE = 100  # 最高分数
MINIMUM_SCORE = 1  # 最低分数
HIGHEST_SCORE = 99  # 范围指定
CHANGE_SCORE = -1  # 减分操作
