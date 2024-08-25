import os
import xml.etree.ElementTree as ET

def convert_float_to_int(value):
    return int(float(value))

def process_xml(xml_file_path, output_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    for obj in root.findall('.//object'):
        for bndbox in obj.findall('.//bndbox'):
            for coord in bndbox:
                coord.text = str(convert_float_to_int(coord.text))

    tree.write(output_file_path)

def convert_all_xmls(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    xml_files = [f for f in os.listdir(input_folder) if f.endswith('.xml')]

    for xml_file in xml_files:
        input_path = os.path.join(input_folder, xml_file)
        output_path = os.path.join(output_folder, xml_file)
        process_xml(input_path, output_path)

# Example usage
input_folder = "F:/wheat_dataset_640x640/annotations/validation"
output_folder = "F:/wheat_dataset_640x640/integer_annot/annotations/validation"

convert_all_xmls(input_folder, output_folder)
