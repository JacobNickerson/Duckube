import re

wanted_text = '<meta content="Dirt is a block found abundantly in most biomes under a layer of grass blocks at the top of the Overworld." name="description"/>'
if matches := re.search(r'meta content="(.+)" name="description"', wanted_text):
    print(matches.group(1))
else:
    print("You didn't find it dipshit")