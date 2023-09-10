import json

from database.models import Author


with open('../files/authors.json') as json_file:
    data = json.load(json_file)

    for i in data:
        Author(
            fullname=i['fullname'],
            born_date=i['born_date'],
            born_location=i['born_location'],
            description=i['description']
        ).save()


