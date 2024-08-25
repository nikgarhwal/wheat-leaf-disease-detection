import xml.etree.ElementTree as ET
import os

xml_folder = "F:/wheat_dataset_512x512/annotations/test"

for filename in os.listdir(xml_folder):
    try:
        xml_path = os.path.join(xml_folder, filename)
        tree = ET.parse(xml_path)
    except Exception as e:
        print(f"Error parsing XML {filename}: {e}")
