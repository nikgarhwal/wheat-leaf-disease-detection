import tensorflow as tf

# Specify the path to the directory containing the events file
log_dir = "C:/Users/friendly/Desktop"

# Load the TensorBoard logs
tensorboard_logs = tf.summary.create_file_writer(log_dir)

# Load the TensorBoard logs and start TensorBoard
tensorboard_logs.set_as_default()

# Load and visualize the TensorBoard logs
tensorboard = tf.summary.create_file_writer(log_dir)

# Start TensorBoard
tensorboard.reload()
