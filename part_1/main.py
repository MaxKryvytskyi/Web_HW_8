from connect_db import connect
from models import Quotes, Authors
from datetime import datetime as DT
from redis_cache import cache


@cache
def case_name(cases):
    result = []
    author_name = " ".join(cases[:]).strip()
    author = Authors.objects(fullname__icontains=author_name).first()
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
    quotes = Quotes.objects(tags__icontains=tag)
    if quotes:
        author_id = quotes[0]["author"]
        for quote in quotes:
            result.append(f"\nTags: {', '.join(quote['tags'])}\nName: {author_id.fullname} \nQuote: {quote['quote']}\n")
    else:
        result.append(f"No tags is {', '.join(tag)}")
    return result


def case_tags(cases):
    result = []
    tags = [tags.strip() for tags in cases[1].split(",")]
    quotes = Quotes.objects(tags__icontains=tags)
    if quotes:
        author_id = quotes[0]["author"]
        for quote in quotes:
            result.append(f"\nTags: {', '.join(quote['tags'])}\nName: {author_id.fullname} \nQuote: {quote['quote']}\n")
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
        
        match cases[0].lower():
            case "name":
                start = DT.now().timestamp()
                results = case_name(cases[1:])
                end = DT.now().timestamp()
                print(f"Результат: {end - start}")

            case "tag":
                results = case_tag(cases)
            case "tags":
                results = case_tags(cases)
            case "exit":
                break
            case _ :
                results = [f"No command {cases[0]}"]
        result(results)
        

if __name__ == "__main__":
    main()




# @cache
# def search_quotes(query):
#     if query.startswith('name: '):
#         author_name = query[6:]
#         author = Authors.objects(fullname__icontains=author_name).first()
#         if author:
#             quotes_ = Quotes.objects(author=author)
#             return quotes_
#     elif query.startswith('tag:'):
#         tag = query[4:]
#         quotes_ = Quotes.objects(tags__icontains=tag)
#         return quotes_
#     elif query.startswith('tags:'):
#         tags = query[5:].split(',')
#         quotes_ = Quotes.objects(tags__in=tags)
#         return quotes_
#     else:
#         return []


# if __name__ == '__main__':
#     while True:
#         user_input = input('Enter command: ')
#         if user_input == 'exit':
#             break


#         start = DT.now().timestamp()
#         quotes = search_quotes(user_input)
#         end = DT.now().timestamp()
#         print(f"Результат: {end - start}")
#         for quote in quotes:
#             author_fullname = quote.author.fullname
#             quote_text = quote.quote
#             author_utf8 = author_fullname.encode('utf-8').decode('utf-8')
#             quote_text_utf8 = quote_text.encode('utf-8').decode('utf-8')

#             print(f'Author: {quote.author.fullname}')
#             print(f'Tags: {", ".join(quote.tags)}.')
#             print(f'Quote: {quote.quote}')
#             print('-'*50)