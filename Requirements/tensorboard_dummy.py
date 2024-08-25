import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Placeholder data for demonstration purposes
(x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape((x_train.shape[0], -1)).astype('float32') / 255.0
y_train = tf.keras.utils.to_categorical(y_train)

# Specify the path to the directory containing the events file
log_dir = "C:/Users/friendly/Desktop"

# Load the TensorBoard logs
tensorboard_logs = tf.summary.create_file_writer(log_dir)

# Create a simple Keras model for demonstration
model = Sequential([Dense(10, input_shape=(784,), activation='softmax')])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Dummy training loop for illustration purposes
for epoch in range(5):
    # Train the model here (replace this with your actual training loop)
    model.fit(x_train, y_train, epochs=1)

    # Log metrics to TensorBoard
    with tensorboard_logs.as_default():
        tf.summary.scalar('accuracy', model.history.history['accuracy'][0], step=epoch)

# Start TensorBoard from the command line
# Open a terminal and navigate to the directory containing the events file
# Run the following command:
# tensorboard --logdir=C:/Users/friendly/Desktop
