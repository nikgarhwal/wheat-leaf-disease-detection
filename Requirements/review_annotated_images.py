import os
import cv2
import xml.etree.ElementTree as ET

def draw_bounding_boxes(image, bounding_boxes, class_names):
    for bbox, class_name in zip(bounding_boxes, class_names):
        x_min, y_min, x_max, y_max = bbox
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 10, 10), 2)
        cv2.putText(image, class_name, (x_min, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 10, 10), 2)
    return image

def read_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    bounding_boxes = []
    class_names = []

    for obj in root.findall('.//object'):
        class_name = obj.find('name').text
        class_names.append(class_name)
        for bndbox in obj.findall('.//bndbox'):
            bbox = [int(bndbox.find(coord).text) for coord in ['xmin', 'ymin', 'xmax', 'ymax']]
            bounding_boxes.append(bbox)

    return bounding_boxes, class_names

def visualize_and_save_images(image_folder, annotation_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    xml_files = [f for f in os.listdir(annotation_folder) if f.endswith('.xml')]

    for xml_file in xml_files:
        image_name = os.path.splitext(xml_file)[0] + '.png'
        image_path = os.path.join(image_folder, image_name)
        xml_path = os.path.join(annotation_folder, xml_file)

        image = cv2.imread(image_path)
        bounding_boxes, class_names = read_xml(xml_path)
        image_with_boxes = draw_bounding_boxes(image.copy(), bounding_boxes, class_names)

        output_path = os.path.join(output_folder, image_name)
        cv2.imwrite(output_path, image_with_boxes)

# Example usage
image_folder = "F:/wheat_dataset_640x640/images/test"
annotation_folder = "F:/wheat_dataset_640x640/annotations/test"
output_folder = "F:/wheat_dataset_640x640_review2/test"

visualize_and_save_images(image_folder, annotation_folder, output_folder)
