# import redis
# from redis_lru import RedisLRU

# client = redis.StrictRedis(host="localhost", port=6379, password=None)
# cache = RedisLRU(client)


# @cache
# def f(x):
#     print(f"Function call f({x})")
#     return x


# if __name__ == '__main__':
#     print(f"Result f(3): {f(3)}")
#     print(f"Result f(3): {f(3)}")
#     print(f"Result f(3): {f(5)}")
#     print(f"Result f(3): {f(5)}")



import pika


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    
    channel.queue_declare(queue='hello_world')
    
    channel.basic_publish(exchange='', routing_key='hello_world', body='Hello world!'.encode())
    print(" [x] Sent 'Hello World!'")
    connection.close()
    

if __name__ == '__main__':
    main()