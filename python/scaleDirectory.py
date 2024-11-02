import os
from PIL import Image
import helper


source_path = input('enter source path:').strip()
destination_path = input('enter destination path:').strip()
width = int(input('enter max width:').strip())
rename_files = helper.valid_input('rename files? ', bool, True, False)

jpeg_compression = 95
save_type = '.png'
save_type = '.jpg'

only_files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]


count = 1
for _file_name in only_files:
    full_source_path = os.path.join(source_path, _file_name)
    full_destination_path = os.path.join(destination_path, _file_name)

    print('Processing:', _file_name)

    if rename_files:
        mod_file_name = _file_name.replace(' ', '_').replace('-1', '').replace('.png', '_thumbnail.png')
        #full_destination_path = os.path.join(destination_path, "card_" + str(count) + ".png")
        full_destination_path = os.path.join(destination_path, mod_file_name)

    if save_type != '':
        full_destination_path = helper.get_full_path_without_extension(full_destination_path) + save_type

    try:
        img = Image.open(full_source_path)
        if save_type == '.jpg':
            img = img.convert('RGB')

        # width
        #width_percent = (width / float(img.size[0]))
        #height_size = int((float(img.size[1]) * float(width_percent)))

        # height
        height = width

        width_percent = (height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(width_percent)))

        # img = img.resize((width, height_size), Image.ANTIALIAS)
        img = img.resize((width_size, height), Image.ANTIALIAS)

        if save_type == '.jpg':
            img.save(full_destination_path, quality=jpeg_compression)
        else:
            img.save(full_destination_path)

        count += 1
        #if width == height_size:
        #    print('Square:', (width, height_size), _file_name)
        #else:
        #    print('NOT Square:', (width, height_size), _file_name)

    except Exception as ex:
        print(ex)
