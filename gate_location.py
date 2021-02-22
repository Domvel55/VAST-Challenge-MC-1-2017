from PIL import Image
import time

import pandas as pd
import numpy as np

map = Image.open("/run/media/sindri/a72af650-e3f6-4184-8000-4d3c78df2267/notes/data vis/Lekagul Roadways.bmp")
map = map.convert("RGB")
count = 0

'''

IMPORTANT:
        the camping sites, coordinates are generated out of ordered,
        and need to be reordered manualy.

'''

color_dict = {
                "ranger-station" : [],
                "entrance" : [],
                "general-gate" : [],
                "gate" : [],
                "camping-spot" : [],
                "ranger-base" : [],
             }




y = 0
while( y < 200):
    x = 0

    while(x < 200):

        pixel = map.getpixel((x,y))
        x += 1

        if(not (pixel == (0,0,0) or pixel == (255,255,255))):

            if(pixel == (255, 216, 0)):
                #ranger stop

                color_dict["ranger-station"].append((x,200 - y))

            elif(pixel == (76, 255, 0)):
                #entrance

                color_dict["entrance"].append((x,200 - y))


            elif(pixel == (0, 255, 255)):
                #general gate

                color_dict["general-gate"].append((x,200 -y))

            elif(pixel == (255, 0 ,0)):
                #gate

                color_dict["gate"].append((x,200 - y))

            elif(pixel == (255, 106 ,0)):
                #camping spot

                color_dict["camping-spot"].append((x,200 - y))

            elif(pixel == (255, 0, 220)):
                #ranger base

                color_dict["ranger-base"].append((x,200 -y))

    y += 1

data = np.empty((40,2))
index = []

count = 0
for item in color_dict:
    print(color_dict[item])
    pos = 0
    while(pos < len(color_dict[item])):

        index.append(item + str(pos))
        data[count] = color_dict[item][pos]
        pos += 1
        count += 1

out = pd.DataFrame(data, index=index, columns=["x","y"])
print(out)
out.to_csv("./gate_location_data_2.csv")
