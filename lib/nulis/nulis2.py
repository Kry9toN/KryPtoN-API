# Module by Krypton-Byte
# https://github.com/krypton-byte/tulis-module

from PIL import Image, ImageDraw, ImageFont
from base64 import b64encode as bs64
output=[]
def tulis2(text):
    '''
    text : string
    '''
    img, font, kata, tempkata=Image.open("lib/nulis/before2.jpg"), ImageFont.truetype("lib/nulis/IndieFlower.ttf",24),'',''
    draw=ImageDraw.Draw(img)
    if type(text) is not list:
        global output
        output=[]
        for i in text:
            if draw.textsize(tempkata, font)[0] < 734:
                tempkata+=i
            else:
                kata, tempkata=kata+'%s\n'%tempkata, i
        if tempkata:
            kata+="%s"%tempkata
        spliter=kata.split("\n")
    else:
        spliter=text
    line=190
    for i in spliter[:25]:
        draw.text((170, int(line)), i, font=font, fill=(0, 0, 0)) #selisih = Line
        line+=37 + 2.2
    print(spliter)
    output.append(img)
    if len(spliter) > 25:
        tulis(spliter[25:])
    return output
