import re
import shutil
import requests


wanted_text = '<meta content="Dirt is a block found abundantly in most biomes under a layer of grass blocks at the top of the Overworld." name="description"/>'
if matches := re.search(r'meta content="(.+)" name="description"', wanted_text):
    print(matches.group(1))
else:
    print("You didn't find it dipshit")

r = requests.get("https://minecraft.wiki/images/Glass_JE4_BE2.png?fb219", stream=True)

if r.status_code == 200:
    with open("images/block.png", "wb") as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)