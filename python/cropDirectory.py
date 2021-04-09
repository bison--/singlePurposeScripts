import cropDirectory_conf as conf
import os
from PIL import Image

sourcePath = input('enter source path:').strip()
if not sourcePath:
    sourcePath = conf.sourcePath

destinationPath = input('enter destination path:').strip()
if not destinationPath:
    destinationPath = conf.sourcePath

onlyFiles = [f for f in os.listdir(sourcePath) if os.path.isfile(os.path.join(sourcePath, f))]

print(onlyFiles)

for _fileName in onlyFiles:
    fullSourcePath = os.path.join(sourcePath, _fileName)
    fullDestinationPath = os.path.join(destinationPath, _fileName)
    im = Image.open(fullSourcePath)
    im_crop = im.crop((conf.startX, conf.startY, conf.endX, conf.endY))
    im_crop.save(fullDestinationPath)
