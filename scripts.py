import requests
from bs4 import BeautifulSoup
import re


def wiki_scrape(item_name):
    found = False
    item_data = {}
    while found == False:
        url = f"https://minecraft.wiki/?search={item_name.replace(" ", "+")}"
        wiki_html = requests.get(url).text
        soup = BeautifulSoup(wiki_html, "html.parser")
        with open("wiki_page.txt", "w", encoding="utf-8") as file:
            file.write(str(soup))

        if redirection := re.search(r"Did you mean: <a href=\"/w/Special:Search\?fulltext=1\&amp;profile=default\&amp;search=([^\"]+)\"", str(soup)):
            item_name = redirection.group(1)
        elif redirection := re.search(r"Showing results for <a href=\"/w/Special:Search\?fulltext=1\&amp;profile=default\&amp;search=([^\"]+)\"", str(soup)):
            item_name = redirection.group(1)
        else:
            found = True
            item_data["url"] = url

    if not_found := re.search(f"<title>Search results for \"{item_name}\" – Minecraft Wiki</title>", str(soup)):
        return {"error": True}
    
    if title := re.search(r"<title>(.+) – Minecraft Wiki</title>", str(soup)):
        item_data["title"] = title.group(1)
    if description := re.search(r"content=\"(.+)\" name=\"description\"", str(soup)):
        item_data["description"] = description.group(1)
    if block_image := re.search(r"content=\"(.+)\" property=\"og:image\"", str(soup)):
        item_data["image"] = block_image.group(1)
    if crafting_recipe := re.search(r"stink butt weiner", str(soup)):
        item_data["crafting_recipe"] = crafting_recipe.group(1)

        

    return item_data


def main():
    block_name = input("Input: ")
    print(wiki_scrape(block_name))


if __name__ == "__main__":
    main()
