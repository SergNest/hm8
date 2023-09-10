import argparse
from functools import wraps

from database.models import Author, Quote


# parser = argparse.ArgumentParser(description='Autors')
#
# parser.add_argument('--action', help='Commands name:, tag:, tags:')
# parser.add_argument('--name')
#
# arguments = vars(parser.parse_args())
#
# action = arguments.get('action')
# name = arguments.get('name')


def find_quote_by_autor(fullname):
    autor = Author.objects(fullname__istartswith=fullname).first()

    quotes = Quote.objects(author=autor)
    for quote in quotes:
        print(quote.quote)


def find_quote_by_tag(tag):
    quotes = Quote.objects(tags__istartswith=tag)
    for quote in quotes:
        print(quote.quote)


def find_quote_by_tags(tags):
    quotes = Quote.objects(tags__in=tags)
    for quote in quotes:
        print(quote.quote)


if __name__ == '__main__':

    while True:
        command = input("Введіть команду: ")
        command_parts = command.split(':')

        if 'exit' in command_parts:
            break

        if len(command_parts) != 2:
            print("Невірний формат команди. Приклад: name: Steve Martin")
            continue

        action = command_parts[0].strip()
        value = command_parts[1].strip()

        if action == 'name':
            find_quote_by_autor(value)
        elif action == 'tag':
            find_quote_by_tag(value)
        elif action == 'tags':
            tags = value.split(',')
            print(tags)
            find_quote_by_tags(tags)
        else:
            print("Невідома команда. Доступні команди: name, tag, tags, exit")