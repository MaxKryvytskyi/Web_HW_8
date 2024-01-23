from web_hw_8.models import Authors, Quotes
from web_hw_8.connect_db import connect
import json


# author = Authors(
#     fullname = "Max Krivitskyh", 
#     born_date = "31.01.1999",
#     born_location = "Kyiv",
#     description = "Buy the super book."
#     )
# author.save()

# quotes = Quotes(
#     tags = ["life","",""],
#     author = "Max Krivitskyh",
#     quote = ""
# )


with open('authors.json', 'r') as file:
    authors_data = json.load(file)

with open('qoutes.json', 'r') as file:
    quotes_data = json.load(file)

for author_data in authors_data:
    author = Authors(**author_data)
    author.save()

for quote_data in quotes_data:
    author_name = quote_data['author']
    author = Authors.objects(fullname=author_name).first()

    if author:
        quote_data['author'] = author
        quote = Quotes(**quote_data)
        quote.save()

