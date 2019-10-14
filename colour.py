import colorgram
from PIL import Image, ImageDraw
import os

# How many palettes we want
paletteCount = 16
# Width and height of the image
width = 1600
height = 800

# Extract 16 colors from an image and return a list
colors = colorgram.extract('dog.jpg', paletteCount)
# Sort by hsl value
colors.sort(key=lambda c: c.hsl.h)

# Work out how wide each band is in pixels (100)
paletteWidth = int(width/paletteCount)

# Create a new base image using the width and height
base_image = Image.new("RGBA", (width, height), None)
# Create a new ImageDraw object so we can draw some rectangles
image = ImageDraw.Draw(base_image)

# Loop through both the list of colours and the width of the image and draw a rectangle for each colour
index = 0
range_increment = 0
while index < len(colors):
    color = colors[index]
    rgb = ((getattr(color.rgb, 'r'), getattr(color.rgb, 'g'), getattr(color.rgb, 'b')))
    image.rectangle([range_increment, 0, range_increment+paletteWidth, height], fill=rgb, outline=None)
    index += 1
    range_increment+=paletteWidth

base_image.save(os.getcwd() + "/testing.png")
