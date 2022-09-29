from PIL import Image

import os
import math

files = [f for f in os.listdir('./input') if os.path.isfile(os.path.join('./input', f))]


columns = len(files)
rows = 1

print("Grid: " + str(columns) + " * " + str(rows))

index = 0

first = Image.open(os.path.join('./input', files[0]))

width = first.width
height = first.height

new_im = Image.new('RGB', (width * columns, height * rows))

for y in range(columns):
    for x in range(columns):
        if index >= len(files):
            break
        im = Image.open(os.path.join('./input', files[index]))
        #im.thumbnail((300,300))
        new_im.paste(im, (x * width, y * height))
        index += 1


current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'output')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)


new_im.save("output/grid.png")

