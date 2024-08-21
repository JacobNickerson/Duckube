import requests
from bs4 import BeautifulSoup
import re
import os
import json

def wiki_scrape(item_name):
    found = False
    item_data = {"error": False}
    while found == False:
        url = f"https://minecraft.wiki/?search={item_name.replace(" ", "+")}"
        wiki_html = requests.get(url).text
        soup = BeautifulSoup(wiki_html, "html.parser")
        
        if redirection := re.search(r"Did you mean: <a href=\"/w/Special:Search\?fulltext=1\&amp;profile=default\&amp;search=([^\"]+)\"", str(soup)):
            item_name = redirection.group(1)
        elif redirection := re.search(r"Showing results for <a href=\"/w/Special:Search\?fulltext=1\&amp;profile=default\&amp;search=([^\"]+)\"", str(soup)):
            item_name = redirection.group(1)
        else:
            found = True
            item_data["url"] = url

    if not_found := re.search(f"<title>Search results for \"{item_name}\" – Minecraft Wiki</title>", str(soup)):
        return {"error": True, "item_name": item_name}
    
    if title := re.search(r"<title>(.+) – Minecraft Wiki</title>", str(soup)):
        item_data["title"] = title.group(1)
    if description := re.search(r"content=\"(.+)\" name=\"description\"", str(soup)):
        item_data["description"] = description.group(1)
    if block_image := re.search(r"content=\"(.+)\" property=\"og:image\"", str(soup)):
        item_data["image"] = block_image.group(1)
    else:
        return {"error": True, "item_name": item_name}

    return item_data

def pull_API_stats():
    url = f"https://api.mcsrvstat.us/3/{os.getenv("minecraft_server_ip")}:{os.getenv("minecraft_server_port")}"
    response = requests.get(url)
    if response.status_code == 200:
        # Parsing the JSON content
        data = response.json()
        return [0, data]
    else:
        return [1, response.status_code]
