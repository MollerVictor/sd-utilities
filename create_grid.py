from PIL import Image

import os
import math

files = [f for f in os.listdir('./input') if os.path.isfile(os.path.join('./input', f))]


biggest_height = 0

for f in files:
    img = Image.open(os.path.join('./input', f))

    biggest_height = max(biggest_height, img.height)

columns = math.ceil(math.sqrt(len(files)))
rows = math.ceil(len(files) / columns)

print("Grid: " + str(columns) + " * " + str(rows))

index = 0

first = Image.open(os.path.join('./input', files[0]))

width = first.width
height = biggest_height

new_im = Image.new('RGB', (width * columns, height * rows))

nexty = 0

for y in range(columns):
    biggest_height_row = 0
    for x in range(columns):
        if index >= len(files):
            break
        im = Image.open(os.path.join('./input', files[index]))
        #im.thumbnail((300,300))
        new_im.paste(im, (x * width, nexty))
        index += 1

        biggest_height_row = max(biggest_height_row, im.height)

    nexty += biggest_height_row


current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'output')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)


new_im.save("output/grid.png")

