import requests
from bs4 import BeautifulSoup
import re


def wiki_scrape(item_name):
    url = f"https://minecraft.wiki/w/{item_name}"
    wiki_html = requests.get(url).text
    data = {}
    soup = BeautifulSoup(wiki_html, "html.parser")
    with open("wiki_page.txt", "w", encoding="utf-8") as file:
        file.write(str(soup))
    if description := re.search(r"content=\"(.+)\" name=\"description\"", str(soup)):
        data["description"] = description.group(1)
    if block_image := re.search(r"content=\"(.+)\" property=\"og:image\"", str(soup)):
        data["image"] = block_image.group(1)
    if crafting_recipe := re.search(r"stink butt weiner", str(soup)):
        data["crafting_recipe"] = crafting_recipe.group(1)
    return data

def main():
    block_name = input("Input: ")
    print(wiki_scrape(block_name))

if __name__ == "__main__":
    main()
