import os


ALLOWED_EXTENSIONS = {'.txt', '.md'}
EXCLUDE_DIR_NAMES = {'example'}


def scan_files(directory, outfile):
    # Write the markdown to the outfile
    with open(outfile, 'w') as md_file:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Only process .txt and .md files
                if file.endswith('.txt') or file.endswith('.md'):
                    # Construct full file path
                    file_path = os.path.join(root, file)
                    # Get folder name
                    folder_name = os.path.basename(root)
                    try:
                        with open(file_path, 'r') as f:
                            # Write the file name and folder name as a H1 header in markdown
                            md_file.write(f'# {folder_name}/{file}\n\n')
                            # Read the file and write its content to the markdown file
                            md_file.write(f.read())
                            md_file.write('\n\n')
                    except Exception as e:
                        print(f'Failed to read file {file_path} due to {e}')


# Call the function with your directory and outfile
scan_files('your_directory_here', 'output/output.md')

