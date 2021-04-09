from os import walk
import hashlib
import time
import datetime
import dupeFilesFinder_conf as conf


def md5sum(filename, block_size=65536):
    hash_instance = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            hash_instance.update(block)
    #return hash.hexdigest()
    return hash_instance.digest()


file_hashes = set()
dupe_count = 0
file_counter = 0

start_time = time.time()
for a_dir in conf.dir_list:
    for (dir_path, dir_names, file_names) in walk(a_dir):
        for file_name in file_names:
            #print(dirpath + file_name)
            #break
            md5 = md5sum(dir_path + "\\" + file_name)
            file_counter += 1
            if md5 not in file_hashes:
                file_hashes.add(md5)
            else:
                dupe_count += 1
                if dupe_count % 1000 == 0:
                    print('file_counter', file_counter, 'dupes:', dupe_count)

duration = time.time() - start_time
print('FINISHED! duration:', str(datetime.timedelta(seconds=round(duration))))
print('files:', file_counter, 'duplicates:', dupe_count)
