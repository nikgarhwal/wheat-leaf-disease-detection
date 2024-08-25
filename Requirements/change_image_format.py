from PIL import Image
import os

# Define the source directory containing images in different formats
source_directory = 'F:/wheat_dataset_new/validation/wheat_mildew_val'

# Define the destination directory where you want to save the converted ".png" images
destination_directory = 'F:/wheat_dataset_format/validation/wheat_mildew_val'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Loop through each image in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith((".jpg", ".jpeg", ".bmp", ".gif", ".tiff")):
        # Check if the file has one of the specified extensions
        file_path = os.path.join(source_directory, filename)

        # Open the image
        image = Image.open(file_path)

        # Convert and save the image as ".png" in the destination directory
        png_file_path = os.path.join(destination_directory, os.path.splitext(filename)[0] + ".png")
        image.save(png_file_path, "PNG")

        # Close the image
        image.close()

print("Image conversion to '.png' format complete.")
