from PIL import Image

import os
import math

files = [f for f in os.listdir('./input') if os.path.isfile(os.path.join('./input', f))]


biggest_height = 0


all_images = []

for f in files:
    img = Image.open(os.path.join('./input', f))

    biggest_height = max(biggest_height, img.height)

    all_images.append(img) 

all_images.sort(key=lambda file: file.height, reverse=True)

columns = math.ceil(math.sqrt(len(all_images)))
rows = math.ceil(len(all_images) / columns)

print("Grid: " + str(columns) + " * " + str(rows))

index = 0

first = all_images[0]

first_img_width = first.width
first_img_height = biggest_height

new_im = Image.new('RGB', (first_img_width * columns, first_img_height * rows))

nexty = 0

for y in range(columns):
    biggest_height_row = 0
    for x in range(columns):
        if index >= len(all_images):
            break
        im = all_images[index]
        #im.thumbnail((300,300))
        new_im.paste(im, (x * first_img_width, nexty))
        index += 1

        biggest_height_row = max(biggest_height_row, im.height)

    nexty += biggest_height_row


#The diff between the guessed height and real height
real_height_diff = (first_img_height * rows) - nexty

#Crops away black at the bottom, that can happen if you use diffrent sized images
new_im = new_im.crop((0, 0, first_img_width * columns, nexty))
newsize = (first_img_width * columns, nexty)
new_im = new_im.resize(newsize)




current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'output')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)


new_im.save("output/grid.png")

