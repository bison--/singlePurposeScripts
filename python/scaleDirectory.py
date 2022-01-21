import os
from PIL import Image

source_path = input('enter source path:').strip()
destination_path = input('enter destination path:').strip()
width = int(input('enter max width:').strip())

only_files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]


count = 1
for _file_name in only_files:
    full_source_path = os.path.join(source_path, _file_name)
    full_destination_path = os.path.join(destination_path, "card_" + str(count) + ".png")

    try:
        img = Image.open(full_source_path)
        width_percent = (width / float(img.size[0]))
        height_size = int((float(img.size[1]) * float(width_percent)))
        img = img.resize((width, height_size), Image.ANTIALIAS)
        img.save(full_destination_path)
        count += 1
    except Exception as ex:
        print(ex)
