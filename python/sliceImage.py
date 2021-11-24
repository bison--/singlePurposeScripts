import os
from PIL import Image

full_source_path = r'C:\Users\Gamer\Pictures\voxel-refs\heightmap_sea_landscape_1024.png'
dest_path = r'output'
source_image = Image.open(full_source_path)  # type: Image.Image

image_size = source_image.size[0]
slice_size = 256

for y in range(0, image_size, slice_size):
    for x in range(0, image_size, slice_size):
        box = (y, x, y + slice_size, x + slice_size)
        sliced = source_image.crop(box)
        sliced.save(os.path.join(dest_path, str(y) + '_' + str(x) + '.png'))
