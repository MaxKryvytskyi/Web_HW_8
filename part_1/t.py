import redis
from redis_lru import RedisLRU
from datetime import datetime
from time import sleep

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
@cache
def fibonacci_cache(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_cache(n-1) + fibonacci_cache(n-2)


if __name__ == '__main__':

    start = datetime.now()
    print(fibonacci(41))
    end = datetime.now()
    print(f"time {end - start}")

    start_cache = datetime.now()
    print(fibonacci_cache(41))
    end_cache = datetime.now()
    print(f"time cache {end_cache - start_cache}")

