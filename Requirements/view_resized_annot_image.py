import os
import random
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Define paths for your resized images and adjusted annotations.
resized_image_folder = "F:/wheat_dataset_512x512/images/test"
adjusted_annotation_folder = "F:/wheat_dataset_512x512/annotations/test"

# Specify the number of random samples to view
num_samples_to_view = 20

# Get a list of image files in the resized image folder
image_files = [f for f in os.listdir(resized_image_folder) if f.endswith(".png")]

# Randomly select a subset of image files
random_samples = random.sample(image_files, num_samples_to_view)

# Iterate through the random sample image files
for sample_image_filename in random_samples:
    # Load the resized image
    sample_image_path = os.path.join(resized_image_folder, sample_image_filename)
    sample_image = Image.open(sample_image_path)

    # Load the corresponding adjusted annotation file
    sample_annotation_filename = sample_image_filename.replace(".png", ".xml")  # Adjust the extension as needed
    sample_annotation_path = os.path.join(adjusted_annotation_folder, sample_annotation_filename)

    # Parse the XML annotation file
    tree = ET.parse(sample_annotation_path)
    root = tree.getroot()

    # Create a Matplotlib figure for the image and bounding boxes
    fig, ax = plt.subplots(1)
    ax.imshow(sample_image)

    # Iterate through the bounding boxes in the annotation and draw them on the image
    for object_elem in root.iter("object"):
        for bbox_elem in object_elem.iter("bndbox"):
            xmin = float(bbox_elem.find("xmin").text)
            ymin = float(bbox_elem.find("ymin").text)
            xmax = float(bbox_elem.find("xmax").text)
            ymax = float(bbox_elem.find("ymax").text)

            # Calculate the coordinates for the adjusted bounding box
            x = xmin
            y = ymin
            width = xmax - xmin
            height = ymax - ymin

            # Create a bounding box rectangle
            rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')

            # Add the rectangle to the image
            ax.add_patch(rect)

    # Set axis properties
    ax.set_xticks([])
    ax.set_yticks([])

    # Display the image with bounding boxes
    plt.show()
