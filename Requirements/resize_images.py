from PIL import Image
import os

# Define the source and destination directories
source_directory = "F:/wheat_dataset/validation/wheat_septoria_val"
destination_directory = "F:/wheat_dataset_new/validation/wheat_septoria_val"

# Define the target size (width, height)
target_size = (1000, 1000)  # Adjust the size as needed

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Loop through each image in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".jpg"):  # Change the file extension as needed
        # Open the image
        image_path = os.path.join(source_directory, filename)
        image = Image.open(image_path)

        # Resize the image to the target size using LANCZOS resampling
        resized_image = image.resize(target_size, Image.LANCZOS)

        # Save the resized image to the destination directory
        destination_path = os.path.join(destination_directory, filename)
        resized_image.save(destination_path)

        # Close the image
        image.close()

print("Image resizing complete.")

