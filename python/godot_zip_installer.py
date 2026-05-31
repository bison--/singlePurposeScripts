import os
import random
import re
import sys
from pathlib import Path
import zipfile


# possible bash alias:
# alias run-update-godot="cd /home/YOUR_HOME/projects/github/singlePurposeScripts/python && python3 godot_zip_installer.py"

# define where the icon is located that should be shown
TEMPLATE_ICON_PATH = "~/Bilder/icons/godot_csharp.png"
# the target folder for the unzipped godot version, I store mine in /home/USER/programs/
UNZIP_PATH = "~/programs"
# the OS-folder that contains all the .dekstop files
TARGET_APP_ICONS_FOLDER = "~/.local/share/applications"


def extract_version(filename: str) -> str | None:
    match = re.search(r'v?(\d+\.\d+\.\d+)', filename)
    return match.group(1) if match else None


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
zip_file = input("Godot ZIP file: ").strip().strip("'")

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
