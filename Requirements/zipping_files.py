import zipfile
import os

def create_zip(input_directory, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        for root, _, files in os.walk(input_directory):
            for file in files:
                # Add each XML file to the zip archive
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, input_directory))

# Example usage:
input_directory = 'F:/wheat_dataset_640x640/annotations/test'
zip_filename = '640_test_xml_annotations.zip'

create_zip(input_directory, zip_filename)
