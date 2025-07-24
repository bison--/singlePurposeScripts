import datetime
import os
import csv
from time import strftime, gmtime
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import helper


source_path = helper.valid_input('Enter path with MP3s:')
dest_csv = helper.valid_input('Enter path and filename for target CSV (default output/track_metadata.csv):', use_default=True, default='output/track_metadata.csv')

csv_handle = open(dest_csv, 'w', encoding='UTF8', newline='\n')
csv_writer = csv.writer(csv_handle)

# header
csv_writer.writerow([
    "Disc Number",
    "Track Number",
    "Original Name",
    "Original Name Language (ie., ""es"", ""jp"") (optional)",
    "International Name (optional)",
    "Duration (""m:ss"")",
    "ISRC (optional)"
])

counter = 0

all_files = os.listdir(source_path)
all_files = sorted(all_files)

for mp3file in all_files:
    if not mp3file.endswith('.mp3'):
        continue

    counter += 1

    file_path = os.path.join(source_path, mp3file)
    audio_tags = EasyID3(file_path)
    audio_stream = MP3(file_path)
    print(audio_tags)

    track_number = counter

    if 'tracknumber' in audio_tags:
        track_number = audio_tags['tracknumber'][0]

    title = audio_tags['title'][0]

    # fix some title issues
    #title = title.replace('Nipple', 'Nibble')

    if '_' in title:
        parts = title.split('_')

        # track numbers are in front
        if parts[0].isnumeric():
            title = ' '.join(parts[1:])
        else:
            title = ' '.join(parts)

    csv_writer.writerow([
        1,
        track_number,
        title,
        'en',
        '',
        #str(datetime.timedelta(seconds=audio_stream.info.length)),
        strftime("%M:%S", gmtime(audio_stream.info.length)),
        ''
    ])

csv_handle.close()
