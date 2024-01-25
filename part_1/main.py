import redis
from redis_lru import RedisLRU
from connect_db import connect
from models import Quotes, Authors
from datetime import datetime as DT

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

@cache
def case_name(cases):
    result = []
    author_name = " ".join(cases[:]).strip()
    author = Authors.objects(fullname=author_name).first()
    if author:
        quotes = Quotes.objects(author=author.id)
        for qoute in quotes:
            result.append(f"\nTags: {', '.join(qoute['tags'])}\nName: {author_name} \nQuote: {qoute['quote']}\n")
    else:
        result.append(f"No author is names {author_name}")
    return result

@cache
def case_tag(cases):
    result = []
    tag = [tag.strip() for tag in cases[1].split(",")]
    quotes = Quotes.objects(tags__in=tag)
    if quotes:
        author_id = quotes[0]["author"]
        for qoute in quotes:
            result.append(f"\nTags: {', '.join(qoute['tags'])}\nName: {author_id.fullname} \nQuote: {qoute['quote']}\n")
    else:
        result.append(f"No tags is {', '.join(tag)}")
    return result

@cache
def case_tags(cases):
    result = []
    tags = [tags.strip() for tags in cases[1].split(",")]
    quotes = Quotes.objects(tags__in=tags)
    if quotes:
        author_id = quotes[0]["author"]
        for qoute in quotes:
            result.append(f"\nTags: {', '.join(qoute['tags'])}\nName: {author_id.fullname} \nQuote: {qoute['quote']}\n")
    else:
        result.append(f"No tags is {', '.join(tags)}")
    return result


def result(results):
    if results:
        for el in results:
            print(el)

def main():
    while True:
        cases = input("---> ").split(":")
        start = DT.now().timestamp()
        match cases[0].lower():
            case "name":
                results = case_name(cases[1:])
            case "tag":
                results = case_tag(cases)
            case "tags":
                results = case_tags(cases)
            case "exit":
                break
            case _ :
                results = [f"No command {cases[0]}"]
        result(results)
        end = DT.now().timestamp()
        print(f"Результат: {end - start}")

if __name__ == "__main__":
    main()