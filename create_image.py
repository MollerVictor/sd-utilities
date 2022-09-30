from PIL import Image

import os
import math
import sys
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# Optional argument
parser.add_argument('--opt-rows', type=int,
                    help='Num of rows it should have.')
parser.add_argument('--no-tight', dest='tight', action='store_false', help='Don\'t compact the images to smallest space.')


args = parser.parse_args()

arg_num_of_rows = args.opt_rows
tight_fit = args.tight



files = [f for f in os.listdir('./input') if os.path.isfile(os.path.join('./input', f))]


biggest_height = 0
biggest_width = 0


all_images = []

for f in files:
    img = Image.open(os.path.join('./input', f))

    biggest_height = max(biggest_height, img.height)
    biggest_width = max(biggest_width, img.width)

    all_images.append(img) 

all_images.sort(key=lambda file: file.height, reverse=True)

rows = math.ceil(math.sqrt(len(all_images)))
if arg_num_of_rows and arg_num_of_rows >= 1:
    rows = arg_num_of_rows

columns = math.ceil(len(all_images) / rows)


print("Tight fit:", tight_fit)
print("Grid:",columns,"*",rows)
print("Rendering...")

index = 0

first = all_images[0]

first_img_width = first.width
first_img_height = biggest_height

new_im = Image.new('RGB', (first_img_width * columns, first_img_height * rows))

nexty = 0

col_current_y = [0] * columns

for y in range(rows):
    biggest_height_row = 0
    for x in range(columns):
        if index >= len(all_images):
            break
        im = all_images[index]        
        
        if tight_fit:
            new_im.paste(im, (x * biggest_width, col_current_y[x]))

            col_current_y[x] += im.height
        else:
            new_im.paste(im, (x * first_img_width, nexty))

        biggest_height_row = max(biggest_height_row, im.height)

        index += 1

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

print("Done")

