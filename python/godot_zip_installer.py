import os
import random
import re
import sys
from pathlib import Path
import requests
import tempfile
import zipfile

import helper

# possible bash alias:
# alias run-update-godot="cd /home/YOUR_HOME/projects/github/singlePurposeScripts/python && python3 godot_zip_installer.py"

# define where the icon is located that should be shown
TEMPLATE_ICON_PATH = "~/Bilder/icons/godot_csharp.png"
# the target folder for the unzipped godot version, I store mine in /home/USER/programs/
UNZIP_PATH = "~/programs"
# the OS-folder that contains all the .dekstop files
TARGET_APP_ICONS_FOLDER = "~/.local/share/applications"

DOWNLOAD_CHUNK_SIZE = 4096

def extract_version(filename: str) -> str | None:
    match = re.search(r'v?(\d+\.\d+\.\d+)', filename)
    return match.group(1) if match else None

def is_valid_version(version):
    if not version:
        return False

    parts = version.split('.')
    for part in parts:
        if not part.isdigit():
            return False

    return True

def get_progress_bar(current, total):
    percentage = current / total * 100
    percentage_int = int(percentage)
    percentage_cut_int = int(percentage / 10)
    return "[" + ("#" * percentage_cut_int).ljust(10) + "] " + str(percentage_int) + " %"

def download_version(version):
    # https://github.com/godotengine/godot/releases/download/4.5.2-stable/Godot_v4.5.2-stable_mono_linux_x86_64.zip
    download_url = f"https://github.com/godotengine/godot/releases/download/{version}-stable/Godot_v{version}-stable_mono_linux_x86_64.zip"
    target_file = os.path.join(tempfile.gettempdir(), f"Godot_v{version}-stable_mono_linux_x86_64.zip")

    if os.path.isfile(target_file):
        print("version", version, "already downloaded to", target_file)
        skip_download = helper.valid_input('skip download? ', bool, True, True)
        if skip_download:
            print("skipping download")
            return target_file

    response = requests.get(download_url, stream=True)
    print("Downloading", download_url, "to", target_file)

    file_size = int(response.headers['content-length'])
    downloaded_size = 0
    downloaded_size_shown = 0
    with open(target_file, "wb") as targe_file_handle:
        for data in response.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE):
            downloaded_size += DOWNLOAD_CHUNK_SIZE
            downloaded_size_shown += DOWNLOAD_CHUNK_SIZE
            if downloaded_size_shown >= 1000000:
                print(f"Downloaded {downloaded_size} / {file_size} bytes")
                print(get_progress_bar(downloaded_size, file_size))
                downloaded_size_shown = 0

            targe_file_handle.write(data)

    print()
    print("Download complete.")

    return target_file


print('''                  
                ==      ==                
            ======     =======            
            ==================            
            ==================            
    ===-  ======================  ====    
   ====================================   
  ======================================  
  ======================================  
   ========---==============---========   
    =====. .:: :==========: ::. .=====    
    ====: =###+ ===:  -=== +###= :====    
    ====- -###+.===-  -===.+###- -====    
    =====-.  ..====-  -====..  .-=====    
    ==================================    
    .......======--------======.......    
    =====: -===== ...... =====- -=====    
    ======  ..... ====== .....  ======    
     =========----======----=========     
      ==============================      
         =======================          
               ============               
''')
print('GODOT version "installer"'.center(42))
print("")

print("HINT: you can drag/drop the file into the terminal")
print("Path (inl. filename) to the ZIP file (e.g. ~/Downloads/Godot_v4.6.3-stable_mono_linux_x86_64.zip)")
print("Version Number: enter a godot version, eg: 4.5.2")
user_input = input("Godot ZIP file OR version number: ").strip().strip("'")

zip_file = ""

if is_valid_version(user_input):
    zip_file = download_version(user_input)
elif user_input.endswith(".zip"):
    zip_file = user_input
else:
    print("Neither a zip file nor a valid version.")
    sys.exit(1)


if zip_file.startswith("~"):
    zip_file = os.path.expanduser(zip_file)

zip_file_name = os.path.basename(zip_file)
program_name = Path(zip_file).stem

UNZIP_PATH = os.path.expanduser(UNZIP_PATH)
TARGET_APP_ICONS_FOLDER = os.path.expanduser(TARGET_APP_ICONS_FOLDER)
TARGET_FILE_PATTERN = "godot-net_{TEMPLATE_VERSION}.desktop"

TEMPLATE_ICON_PATH = os.path.expanduser(TEMPLATE_ICON_PATH)
TEMPLATE_PATH = os.path.expanduser(os.path.join(UNZIP_PATH, program_name))
TEMPLATE_EXEC_PATH = os.path.join(TEMPLATE_PATH, program_name.replace("_x86_64", ".x86_64"))
TEMPLATE_VERSION = extract_version(program_name)  #4.6.0


# https://specifications.freedesktop.org/desktop-entry/1.2/recognized-keys.html

TEMPLATE = '''[Desktop Entry]
Type=Application
Name=Godot C# {TEMPLATE_VERSION}
GenericName=Game Engine
Icon={TEMPLATE_ICON_PATH}
Exec={TEMPLATE_EXEC_PATH}
Path={TEMPLATE_PATH}
Categories=Development
Terminal=false
StartupNotify=false
X-GNOME-Autostart-enabled=false
X-AppImage-Integrate=false
'''

# check if everything is okay

if not os.path.isdir(UNZIP_PATH):
    print("UNZIP_PATH the unzip target path doesn't exist: ", UNZIP_PATH)
    sys.exit(1)

if not os.path.isfile(TEMPLATE_ICON_PATH):
    print("TEMPLATE_ICON_PATH the icon doesn't exist: ", TEMPLATE_ICON_PATH)
    sys.exit(1)

if not TEMPLATE_VERSION:
    print("TEMPLATE_VERSION not found: ", TEMPLATE_VERSION)
    sys.exit(1)

if not TARGET_APP_ICONS_FOLDER:
    print("Folder for .desktop files not found: ", TARGET_APP_ICONS_FOLDER)
    sys.exit(1)


with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(UNZIP_PATH)

# make godot executable
os.chmod(TEMPLATE_EXEC_PATH, 0o766)

desktop_file_content = TEMPLATE.format(
    TEMPLATE_VERSION=TEMPLATE_VERSION,
    TEMPLATE_ICON_PATH=TEMPLATE_ICON_PATH,
    TEMPLATE_EXEC_PATH=TEMPLATE_EXEC_PATH,
    TEMPLATE_PATH=TEMPLATE_PATH,
)

desktop_file_target = os.path.join(
    TARGET_APP_ICONS_FOLDER,
    TARGET_FILE_PATTERN.format(TEMPLATE_VERSION=TEMPLATE_VERSION.replace(".", "_"))
)

open(desktop_file_target, mode='w').write(desktop_file_content)

print("All done.")
print("It should show up on the last page of your desktop application icon page.")
print("If not, you can try refreshing the icon cache:")
print("update-desktop-database ~/.local/share/applications")
print("refresh-icons")
print("")
print("Have a nice day", random.choice(["o/", "<3", "☞ﾟ∀ﾟ)☞", "( ﾉ^ω^)ﾉﾟ", "└(°ᴗ°)┘", "\\ ( ^ ▽ ^ ) /"]))
