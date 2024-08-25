import os
import xml.etree.ElementTree as ET
from PIL import Image

# Define paths for your source images, annotations, and destination for resized images and adjusted annotations.
source_image_folder = "F:/wheat_dataset_512x512/images/train"
source_annotation_folder = "F:/wheat_dataset_512x512/annotations/train"
output_image_folder = "F:/wheat_dataset_640x640_2/images/train"
output_annotation_folder = "F:/wheat_dataset_640x640_2/annotations/train"

# Desired new image size
new_size = (640, 640)

# Create the output directories if they don't exist
os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_annotation_folder, exist_ok=True)

# Iterate through the image files
for image_filename in os.listdir(source_image_folder):
    # Load the image
    image_path = os.path.join(source_image_folder, image_filename)
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Load the corresponding annotation file
    annotation_filename = image_filename.replace(".png", ".xml")  # Adjust the extension as needed
    annotation_path = os.path.join(source_annotation_folder, annotation_filename)

    # Parse the XML annotation file
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    # Update the image size in the annotation
    for size_elem in root.iter("size"):
        for width_elem in size_elem.iter("width"):
            width_elem.text = str(new_size[0])
        for height_elem in size_elem.iter("height"):
            height_elem.text = str(new_size[1])

    # Resize the image
    resized_image = image.resize(new_size)
    resized_image.save(os.path.join(output_image_folder, image_filename))

    # Adjust the bounding box coordinates in the annotation
    for object_elem in root.iter("object"):
        for bbox_elem in object_elem.iter("bndbox"):
            for coord in ["xmin", "ymin", "xmax", "ymax"]:
                coord_elem = bbox_elem.find(coord)
                coord_value = float(coord_elem.text)  # Change to float
                if coord in ["xmin", "xmax"]:
                    coord_value = coord_value * (new_size[0] / image_width)
                else:
                    coord_value = coord_value * (new_size[1] / image_height)
                coord_elem.text = str(coord_value)

    # Save the adjusted annotation
    adjusted_annotation_path = os.path.join(output_annotation_folder, annotation_filename)
    tree.write(adjusted_annotation_path)

print("Images and annotations resized and adjusted.")






