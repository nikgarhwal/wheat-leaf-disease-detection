import tensorflow as tf
import matplotlib.pyplot as plt
import os

# Load the original image
img_path = "F:/wheat_dataset_640x640/images/train/Brust2448.png"  # Replace with the actual path to your image
img = tf.io.read_file(img_path)
img = tf.image.decode_jpeg(img, channels=3)

# Configure data augmentations
data_augmentation_options = {
    'horizontal_flip': tf.image.random_flip_left_right,
    'vertical_flip': tf.image.random_flip_up_down,
    'random_crop': lambda x: tf.image.random_crop(x, size=[640, 640, 3]),
    'random_adjust_hue': lambda x: tf.image.random_hue(x, max_delta=0.3),
    'random_adjust_contrast': lambda x: tf.image.random_contrast(x, lower=0.2, upper=2.0),
    'random_adjust_saturation': lambda x: tf.image.random_saturation(x, lower=0.2, upper=2.0),
    'random_adjust_brightness': lambda x: tf.image.random_brightness(x, max_delta=0.4),
    'scale_crop_and_pad_to_square': lambda x: tf.image.central_crop(tf.image.random_crop(x, size=[600, 600, 3]))
}

# Ensure the directory exists
save_dir = "F:/augmented_images"  # Replace with the desired directory path
os.makedirs(save_dir, exist_ok=True)

# Apply data augmentations and save augmented images
for aug_name, aug_fn in data_augmentation_options.items():
    augmented_img = aug_fn(img)
    
    # Display the augmented image
    plt.imshow(augmented_img.numpy().astype(int))
    plt.title(f'{aug_name} Augmentation')
    plt.axis('off')
    plt.show()

    # Save the augmented image
    save_path = os.path.join(save_dir, f'{aug_name}_augmented.jpg')
    tf.keras.preprocessing.image.save_img(save_path, augmented_img.numpy())
    print(f'{aug_name} Augmented Image saved at: {save_path}')

