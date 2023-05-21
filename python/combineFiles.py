import os
import argparse

ALLOWED_EXTENSIONS = {'.txt', '.md'}
EXCLUDE_FOLDER_NAMES = {'example', 'examples', 'blog', 'roadmap'}


def scan_files(directory, outfile):
    # Write the markdown to the outfile
    with open(outfile, 'w') as md_file:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            # Skip directories in EXCLUDE_DIR_NAMES
            dirs[:] = [d for d in dirs if d not in EXCLUDE_FOLDER_NAMES]
            for file in files:
                # Get the file extension
                _, ext = os.path.splitext(file)
                # Only process files with allowed extensions
                if ext in ALLOWED_EXTENSIONS:
                    # Construct full file path
                    file_path = os.path.join(root, file)
                    # Get folder name
                    folder_name = os.path.basename(root)
                    try:
                        with open(file_path, 'r') as f:
                            print('Reading:', file_path)
                            # Write the file name and folder name as a H1 header in markdown
                            md_file.write(f'# {folder_name}/{file}\n\n')
                            # Read the file and write its content to the markdown file
                            md_file.write(f.read())
                            md_file.write('\n\n')
                    except Exception as e:
                        print(f'Failed to read file {file_path} due to {e}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Combine files into a markdown file.')
    parser.add_argument('--directory', type=str, default='your_directory_here',
                        help='the directory to scan')
    parser.add_argument('--outfile', type=str, default='output.md',
                        help='the markdown file to write to')
    args = parser.parse_args()

    scan_files(args.directory, args.outfile)
