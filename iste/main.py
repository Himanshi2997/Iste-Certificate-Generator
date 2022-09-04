# importing packages & modules
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Implementation to generate certificate
df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf', 30)
for index, j in df.iterrows():
    img = Image.open('picture.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(500, 400),
              text='{}'.format(j['name']),
              fill=(0, 0, 0),
              font=font)  # customization
    img.save('pictures/{}.jpg'.format(j['name']))
