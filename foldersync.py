import os
import shutil
from filecmp import dircmp
import argparse

def sync_folders(source, destination):
    if not os.path.exists(source):
        raise ValueError(f"Source folder '{source}' does not exist.")
    
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    compare_folders(source, destination)

def compare_folders(source, destination):
    comparison = dircmp(source, destination)
    
    # Copy files from source to destination
    for file_name in comparison.left_only:
        source_path = os.path.join(source, file_name)
        dest_path = os.path.join(destination, file_name)
        
        if os.path.isdir(source_path):
            shutil.copytree(source_path, dest_path)
            print(f"Directory copied from {source_path} to {dest_path}")
        else:
            shutil.copy2(source_path, dest_path)
            print(f"File copied from {source_path} to {dest_path}")
    
    # Recursively synchronize subdirectories
    for common_dir in comparison.common_dirs:
        compare_folders(
            os.path.join(source, common_dir),
            os.path.join(destination, common_dir)
        )
    
    # Remove files and directories that are only in the destination
    for file_name in comparison.right_only:
        dest_path = os.path.join(destination, file_name)
        if os.path.isdir(dest_path):
            shutil.rmtree(dest_path)
            print(f"Directory removed: {dest_path}")
        else:
            os.remove(dest_path)
            print(f"File removed: {dest_path}")

def main():
    parser = argparse.ArgumentParser(description='Synchronize two folders to maintain consistency.')
    parser.add_argument('source', type=str, help='The source folder to synchronize from.')
    parser.add_argument('destination', type=str, help='The destination folder to synchronize to.')
    
    args = parser.parse_args()
    
    try:
        sync_folders(args.source, args.destination)
        print("Synchronization complete.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()