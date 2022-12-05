from PIL import Image
import os

current_dir = os.getcwd()
# Open the image and convert it to grayscale
im = Image.open(current_dir + '/img/stop.png').convert('L')

# Resize the image to a specified width
width = 100
im = im.resize((width, int(im.height * width / im.width)))

# Loop through each pixel and create a character representation
for y in range(im.height):
    for x in range(im.width):
        # Get the grayscale value of the pixel
        gray = im.getpixel((x, y))

        # Choose a character to represent the grayscale value
        if gray < 10:
            char = ' '
        elif gray < 20:
            char = '.'
        elif gray < 30:
            char = '-'
        elif gray < 40:
            char = ':'
        elif gray < 50:
            char = '*'
        elif gray < 60:
            char = '+'
        elif gray < 70:
            char = '?'
        elif gray < 80:
            char = 'X'
        else:
            char = '#'

        # Print the character on the screen
        print(char, end='')
    print()
