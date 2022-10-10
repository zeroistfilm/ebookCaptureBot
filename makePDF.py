import os
from PIL import Image
title='취미로해킹'
filenameList = [i for i in os.listdir(f'./{title}')]
filenameList.sort(key=len)
imageList = []
for filename in filenameList:
    img = Image.open(f"./{title}/{filename}")
    imageList.append(img.convert('RGB'))
imageList[0].save(f'./{title}.pdf', save_all=True, append_images=imageList[1:], quality=100)
