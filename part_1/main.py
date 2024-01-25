from connect_db import connect
from models import Quotes, Authors
from work_speed import work_speed
from redis_cache import cache

@work_speed
@cache
def case_name(cases):
    author_name = " ".join(cases[:]).strip()
    author = Authors.objects(fullname__icontains=author_name).first()
    if author:
        quotes = Quotes.objects(author=author.id)
        return quotes
    else:
        return []

@work_speed
@cache
def case_tag(cases):
    tag = [tag.strip() for tag in cases[1].split(",")]
    quotes = Quotes.objects(tags__in=tag)
    return quotes

@work_speed
@cache
def case_tags(cases):
    tags = [tags.strip() for tags in cases[1].split(",")]
    quotes = Quotes.objects(tags__in=tags)
    return quotes

@cache
def print_result(quotes, cases):
    if quotes:
        print("_" * 50)
        for quote in quotes:
            author_id = quote["author"]
            print(f"Author: {author_id.fullname} \nTags: {', '.join(quote['tags'])}\nQuote: {quote['quote']}")
            print("_" * 50)
    else:
        print(f"{cases[0]}: {cases[1:][0]} no found")

def main():
    while True:
        cases = input("---> ").split(":")
        match cases[0].lower():
            case "name":
                print_result(case_name(cases[1:]), cases)
            case "tag":
                print_result(case_tag(cases), cases)
            case "tags":
                print_result(case_tags(cases), cases)
            case "exit":
                break
            case _ :
                print(f"No command {cases[0]}:")
        

if __name__ == "__main__":
    main()