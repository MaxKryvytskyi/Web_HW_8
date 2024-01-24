from connect_db import connect
from models import Quotes, Authors


def case_name(cases):
    author_name = " ".join(cases[:]).strip()
    author = Authors.objects(fullname=author_name).first()
    if author:
        quotes = Quotes.objects(author=author.id)
        for qoute in quotes:
            print(f"\nTags: {', '.join(qoute['tags'])}\nName: {author_name} \nQuote: {qoute['quote']}\n")
    else:
        print(f"No author is names {author_name}")


def case_tag(cases):
    tag = [tag.strip() for tag in cases[1].split(",")]
    quotes = Quotes.objects(tags__in=tag)
    if quotes:
        author_id = quotes[0]["author"]
        for qoute in quotes:
            print(f"\nTags: {', '.join(qoute['tags'])}\nName: {author_id.fullname} \nQuote: {qoute['quote']}\n")
    else:
        print(f"No tags is {', '.join(tag)}")


def case_tags(cases):
    tags = [tags.strip() for tags in cases[1].split(",")]
    quotes = Quotes.objects(tags__in=tags)
    if quotes:
        author_id = quotes[0]["author"]
        for qoute in quotes:
            print(f"\nTags: {', '.join(qoute['tags'])}\nName: {type(author_id.fullname)} \nQuote: {qoute['quote']}\n")
    else:
        print(f"No tags is {', '.join(tags)}")


def main():
    while True:
        cases = input("---> ").split(":")
        match cases[0].lower():
            case "name":
                case_name(cases[1:])
            case "tag":
                case_tag(cases)
            case "tags":
                case_tags(cases)
            case "exit":
                break
            case _ :
                print(f"No command {cases[0]}")

if __name__ == "__main__":
    main()