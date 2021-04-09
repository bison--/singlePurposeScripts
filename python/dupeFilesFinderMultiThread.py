from os import walk
import hashlib
import time
import datetime
import concurrent.futures
import dupeFilesFinder_conf as conf


def md5sum(filename, block_size=65536):
    hash_instance = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            hash_instance.update(block)
    #return hash.hexdigest()
    return hash_instance.digest()


def multi_thread_md5(full_path):
    md5_digest = md5sum(full_path)
    return md5_digest


file_hashes = set()
all_file_paths = set()
dupe_count = 0

start_time = time.time()
print('collecting files')
for a_dir in conf.dir_list:
    for (dir_path, dir_names, file_names) in walk(a_dir):
        for file_name in file_names:
            all_file_paths.add(dir_path + "\\" + file_name)
            #print(dirpath + file_name)
            #break

file_counter = len(all_file_paths)
print('files to check:', file_counter)

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    all_md5s = executor.map(multi_thread_md5, all_file_paths)

print('start comparison')
for md5 in all_md5s:
    if md5 not in file_hashes:
        file_hashes.add(md5)
    else:
        dupe_count += 1
        if dupe_count % 1000 == 0:
            print('file_counter', file_counter, 'dupes:', dupe_count)


duration = time.time() - start_time
print('FINISHED! duration:', str(datetime.timedelta(seconds=round(duration))))
print('files:', file_counter, 'duplicates:', dupe_count)
