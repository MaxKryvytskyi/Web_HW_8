
from connect_db import connect
from models import Quotes, Authors
from pprint import pprint

def main():
    while True:
        cases = input("---> ").split(" ")

        name = " ".join(cases[1::])
        match cases[0]:
            case "name:":
                author = Authors.objects(fullname=name).first()
                quotess = Quotes.objects.filter(author=author.id)
                print(len(quotess))
                for qoutes in quotess:
                    pprint(f"{qoutes['tags']} {name} {qoutes['quote']}")
                print("name:")
            case "tag:":
                print("tag:")
            case "tags:":
                print("tags:")
            case "exit":
                break

if __name__ == "__main__":
    main()