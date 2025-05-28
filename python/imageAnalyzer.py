#!/usr/bin/env python3

import os
import argparse
from collections import Counter
from PIL import Image


def human_readable_size(size, decimal_places=2):
    """
    Convert a file size in bytes to a human-readable string.
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0 or unit == 'TB':
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024.0


def gather_image_stats(root_dir, ext):
    """
    Traverse root_dir recursively, collecting image resolution counts and file sizes
    for all files matching the extension ext.

    Returns:
        resolution_counter (Counter): counts of (width, height) tuples
        file_sizes (list): list of file sizes in bytes
        total_files (int): total number of files processed
    """
    resolution_counter = Counter()
    file_sizes = []
    total_files = 0

    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if not fname.lower().endswith(ext.lower()):
                continue
            total_files += 1
            file_path = os.path.join(dirpath, fname)
            try:
                with Image.open(file_path) as img:
                    resolution_counter[img.size] += 1
            except Exception as e:
                print(f"Warning: Could not open {file_path}: {e}")
                continue

            try:
                size_bytes = os.path.getsize(file_path)
                file_sizes.append(size_bytes)
            except OSError as e:
                print(f"Warning: Could not get size for {file_path}: {e}")

    return resolution_counter, file_sizes, total_files


def analyze_image_directory(directory, ext='.png'):
    """
    Analyze image files in a directory and return statistics.

    Args:
        directory (str): path to the root directory
        ext (str): image file extension (e.g., '.png')

    Returns:
        dict: {
            'total_files': int,
            'min_size': int,
            'max_size': int,
            'total_size': int,
            'resolution_counts': Counter
        }
    """
    res_counts, sizes, total_files = gather_image_stats(directory, ext)

    return {
        'total_files': total_files,
        'min_size': min(sizes) if sizes else 0,
        'max_size': max(sizes) if sizes else 0,
        'total_size': sum(sizes) if sizes else 0,
        'resolution_counts': res_counts
    }


def print_stats(stats):
    """
    Print the image statistics in a human-readable form.
    """
    print(f"Total image files found: {stats['total_files']}")

    if stats['total_files'] > 0:
        print(f"Minimum file size: {human_readable_size(stats['min_size'])}")
        print(f"Maximum file size: {human_readable_size(stats['max_size'])}")
        print(f"Total file size: {human_readable_size(stats['total_size'])}")
    else:
        print("No file size data available.")

    if stats['resolution_counts']:
        print("\nImage resolutions count:")
        for (w, h), count in sorted(stats['resolution_counts'].items()):
            print(f"{w}x{h}: {count}")
    else:
        print("No resolution data available.")


def resize_images(root_dir, ext, percentage, output_dir=None):
    """
    Resize images proportionally by a percentage.

    Args:
        root_dir (str): directory to search for images
        ext (str): image file extension (e.g., '.png')
        percentage (float): resize factor in percent (e.g., 50 for 50%)
        output_dir (str, optional): directory to save resized images;
            if None, original files will be overwritten.

    Returns:
        int: number of images resized
    """
    factor = percentage / 100.0
    count = 0

    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if not fname.lower().endswith(ext.lower()):
                continue
            src_path = os.path.join(dirpath, fname)
            try:
                with Image.open(src_path) as img:
                    new_size = (int(img.width * factor), int(img.height * factor))
                    resized = img.resize(new_size, Image.LANCZOS)

                    # Determine save path
                    if output_dir:
                        rel_path = os.path.relpath(dirpath, root_dir)
                        target_dir = os.path.join(output_dir, rel_path)
                        os.makedirs(target_dir, exist_ok=True)
                        dest_path = os.path.join(target_dir, fname)
                    else:
                        dest_path = src_path

                    resized.save(dest_path)
                    count += 1
            except Exception as e:
                print(f"Warning: Could not resize {src_path}: {e}")
    return count


def main():
    parser = argparse.ArgumentParser(
        description="Analyze and optionally resize image files in a directory."
    )
    parser.add_argument('directory', help="Root directory to search for images")
    parser.add_argument('--ext', default='.png', help="Image file extension (default: .png)")
    parser.add_argument(
        '--resize', type=float,
        help="Resize images by percentage (e.g., 50 for 50%)"
    )
    parser.add_argument(
        '--output-dir', default=None,
        help="Directory to save resized images (overwrites originals if omitted)"
    )
    args = parser.parse_args()

    stats = analyze_image_directory(args.directory, args.ext)
    print_stats(stats)

    if args.resize:
        num = resize_images(
            args.directory, args.ext, args.resize, args.output_dir
        )
        print(f"\nResized {num} image(s) by {args.resize}%.")


if __name__ == '__main__':
    #main()
    imageDir = r"K:\gamedev\godot\streamerFlowers\streameFlowers\images\flowers\moonflower_v3_parts"
    stats = analyze_image_directory(imageDir)
    print_stats(stats)
    '''
    num = resize_images(
        imageDir,
        ".png",
        50
    )

    stats = analyze_image_directory(imageDir)
    print_stats(stats)
    '''
