"""
这是数据库模块
这里提供所有数据库操作的方法
"""

import random
import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DATABASE, REDIS_OBJECT
from config import INIT_SCORE, HIGH_SCORE, MINIMUM_SCORE, HIGHEST_SCORE, CHANGE_SCORE

class RedisClient:
    """这是一个数据库的类，里面提供了用于操作数据库的所有的方法"""

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DATABASE):
        """初始化redis数据库的连接"""
        """在这里定义host，端口，和要操作的数据库名字"""
        self.db = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def exists(self, proxy):
        """判断传入的ip地址（代理），看看有没有已经存在数据库中"""
        return not self.db.zscore(REDIS_OBJECT, proxy) is None

    def add(self, proxy, score=INIT_SCORE):
        """
        添加ip地址（代理）到数据库，并将代理的分数进行初始化赋值
        :param proxy:    传进来的代理ip地址
        :param score:    初始化的分数
        """
        if not self.exists(proxy):
            return self.db.zadd(REDIS_OBJECT, {proxy: score})

    def random(self):
        """随机选择一个代理"""
        # 1.尝试获取评分最高的代理（可能有多个）
        proxies = self.db.zrangebyscore(REDIS_OBJECT, HIGH_SCORE, HIGH_SCORE)
        if len(proxies):
            return random.choice(proxies)
        # 2.没有评分在100分的代理，尝试获取最低分到99分之间的代理
        proxies = self.db.zrangebyscore(REDIS_OBJECT, INIT_SCORE, HIGHEST_SCORE)
        if len(proxies):
            return random.choice(proxies)
        # 3.最后一种情况，没有查询到代理
        print('数据库为空')

    def decrease(self, proxy):
        """定义降低分数的方法，如果代理检测不过关，则降低代理的分数"""
        self.db.zincrby(REDIS_OBJECT, CHANGE_SCORE, proxy)
        score = self.db.zscore(REDIS_OBJECT, proxy)
        if score <= MINIMUM_SCORE:
            self.db.zrem(REDIS_OBJECT, proxy)

    def max(self, proxy):
        """如果监测的代理可用，则将该代理的分数设置为100"""
        return self.db.zadd(REDIS_OBJECT, {proxy: HIGH_SCORE})

    def count(self):
        """获取当前具有代理的数量"""
        return self.db.zcard(REDIS_OBJECT)

    def all(self):
        """直接获取所有的代理"""
        # 首先判断数据库中有没有代理的数据
        proxies = self.db.zrangebyscore(REDIS_OBJECT, MINIMUM_SCORE, HIGH_SCORE)
        if proxies:
            return proxies
        else:
            print('数据库为空')

    def count_for_num(self, number):
        """指定数量获取代理，并返回的是一个列表"""
        all_proxy = self.all()  # 首先直接调用上面的all函数，直接获取所有的代理，保存到all_proxy变量中
        proxies = random.sample(all_proxy, k=number)
        return proxies


if __name__ == '__main__':
    proxy = []
    redis_client = RedisClient()
