import os
from PIL import Image
from datetime import datetime

for image_file_name in os.listdir('./imgs/'):
    if image_file_name.endswith('.png'):
        now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')

        im = Image.open('./crop/' + image_file_name)
        box = (50, 50, 1000, 650)
        im = im.crop(box)
        im.save('./resize/' + now + '.png')
