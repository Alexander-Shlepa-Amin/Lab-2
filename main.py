import csv
import random
from collections import Counter
import xml.dom.minidom as minidom


def count_long_titles():
    cnt = 0
    with open("books.csv") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            title = row.get("Название", "")
            if len(title) > 30:
                cnt += 1
    return cnt


def find_books(author):
    res = []
    with open("books.csv") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            book_author = row.get("Автор", "")
            if author.lower() in book_author.lower():
                price = float(row.get("Цена", "0").replace(",", "."))
                if price <= 150:
                    res.append(row)
    return res


def make_refs():
    with open("books.csv") as f:
        books = list(csv.DictReader(f, delimiter=";"))

    chosen = random.sample(books, 20)
    with open("result.txt", "w", encoding="utf-8") as out:
        for i, b in enumerate(chosen, 1):
            author = b.get("Автор", "")
            title = b.get("Название", "")
            year = b.get("Год", "")
            out.write(f"{i}. {author}. {title} - {year}\n")


def parse_currency():
    dom = minidom.parse("currency.xml")
    valutes = dom.getElementsByTagName("Valute")
    rates = {}
    for v in valutes:
        name = v.getElementsByTagName("Name")[0].firstChild.data
        val = float(v.getElementsByTagName("Value")[0].firstChild.data.replace(",", "."))
        rates[name] = val
    return rates


def get_tags():
    dom = minidom.parse("currency.xml")
    tags = set()
    for node in dom.getElementsByTagName("*"):
        tags.add(node.tagName)
    return tags


def top_books():
    with open("books.csv",  ) as f:
        titles = [row.get("Название", "") for row in csv.DictReader(f, delimiter=";")]
    return Counter(titles).most_common(20)


if __name__ == "__main__":
    print("Книг с длинным названием:", count_long_titles())
    print("Поиск автора (до 150р):", len(find_books("")))
    make_refs()
    print("Валюты:", parse_currency())
    print("Теги:", get_tags())
    print("Топ-20:", top_books())