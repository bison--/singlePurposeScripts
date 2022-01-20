from PIL import Image, ImageFont, ImageDraw
text_font = ImageFont.truetype('temp/ComicNeue-Regular.ttf', 200)
input_file = 'temp/frame_wood2.png'

for i in range(1, 23):
    text = str(i)
    image = Image.open(input_file)
    image_editable = ImageDraw.Draw(image)
    image_editable.text((600, 640), text, (237, 230, 211), font=text_font)
    image.save('output/card_'+text+'.png')
