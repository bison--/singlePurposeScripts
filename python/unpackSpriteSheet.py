import unpackSpriteSheet_conf as conf
import os
from PIL import Image

destinationPath = 'output'

fullSourcePath = input('enter source file:')
if not fullSourcePath:
    fullSourcePath = conf.sourceFile

fileName = os.path.basename(fullSourcePath)
fileNameWithoutExtension, fileExtension = os.path.splitext(fileName)

# ~PIL.Image.Image
im: Image.Image = Image.open(fullSourcePath)

imageWidth = im.width
imageHeight = im.height

# horizontal / row->column extraction
for y in range(int(imageHeight / conf.height)):
    for x in range(int(imageWidth / conf.width)):
        im_crop = im.crop((
            x * conf.width, y * conf.height,
            (x + 1) * conf.width, (y + 1) * conf.height))

        fullDestinationPath = os.path.join(destinationPath, '{0}_{1}_{2}{3}'.format(fileNameWithoutExtension, y, x, fileExtension))
        im_crop.save(fullDestinationPath)

#im_crop = im.crop((conf.startX, conf.startY, conf.endX, conf.endY))
#im_crop.save(fullDestinationPath)