import requests
from bs4 import BeautifulSoup
import re


def wiki_scrape(item_name):
    url = f"https://minecraft.wiki/w/{item_name}"
    response = requests.get(url)
    return response.text


def wiki_parse(wiki_html):
    data = []
    soup = BeautifulSoup(wiki_html, "html.parser")
    with open("wiki_page.txt", "w", encoding="utf-8") as file:
       file.write(str(soup))
    if description := re.search(r"content=\"(.+)\" name=\"description\"", str(soup)):
       data.append(description.group(1))
    if block_image := re.search(r"content=\"(.+)\" property=\"og:image\"", str(soup)):
       data.append(block_image.group(1))
    else:
        print("DIE")
    return data

def main():
    block_name = input("Input: ")
    print(wiki_parse(wiki_scrape(block_name)))


if __name__ == "__main__":
    main()
