from PIL import Image
import os

def is_corrupted_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.load()
        return False
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return True

def find_corrupted_files(directory):
    corrupted_files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if is_corrupted_image(file_path):
            corrupted_files.append(file_path)
    return corrupted_files

directory_path = 'F:/wheat_dataset_512x512/images/validation'  # Replace with the path to your directory
corrupted_files = find_corrupted_files(directory_path)

if corrupted_files:
    print("Corrupted files:")
    for file_path in corrupted_files:
        print(file_path)
else:
    print("No corrupted files found.")
