from pymongo import MongoClient
from pymongo.server_api import ServerApi

import database.db
from database.models import Cats, Author, Quote

# autor = Author.objects(fullname='Albert Einstein')

autor = Author.objects(fullname='Albert Einstein').first()

quotes = Quote.objects(author=autor)
for quote in quotes:
    print(quote.quote)

# client = MongoClient(
#     "mongodb+srv://mongo_user:IcwO1FuM82chPgov@mycluster0.e6xyj9t.mongodb.net/?retryWrites=true&w=majority",
#     server_api=ServerApi('1')
# )

# db = client.book

# result_one = db.cats.insert_one(
#     {
#         "name": "barsik",
#         "age": 3,
#         "features": ["ходить в капці", "дає себе гладити", "рудий"],
#     }
# )
#
# print(result_one.inserted_id)
#
# result_many = db.cats.insert_many(
#     [
#         {
#             "name": "Lama",
#             "age": 2,
#             "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
#         },
#         {
#             "name": "Liza",
#             "age": 4,
#             "features": ["ходить в лоток", "дає себе гладити", "білий"],
#         },
#     ]
# )
# print(result_many.inserted_ids)

# r = db.cats.find()
# print(r)
# for i in r:
#     print(i)













