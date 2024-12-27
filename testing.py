import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

# Load the saved model
model = tf.keras.models.load_model('custom_resnet_lung_model.keras')

# Define image dimensions expected by the model
img_height = 128  # Adjusted to match model's expected input size
img_width = 128   # Adjusted to match model's expected input size

# Function to load and preprocess an image
def load_and_preprocess_image(img_path, img_height, img_width):
    img = image.load_img(img_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Rescale the image
    return img_array

# Function to display the image and its predicted class
def predict_and_display(img_path, img_height, img_width):
    img_array = load_and_preprocess_image(img_path, img_height, img_width)
    prediction = model.predict(img_array)
    
    # Get the predicted class
    predicted_class = np.argmax(prediction, axis=1)[0]
    
    # Class names (adjust according to your dataset)
    class_names = [ 'Lung Adenocarcinoma', 'Lung Benign Tissue','Lung Squamous Cell Carcinoma']
    
    # Display the image and the prediction
    img = image.load_img(img_path)
    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Predicted: {class_names[predicted_class]}\n")
    plt.show()

# List of image paths you want to predict
image_paths = [
    'C:/Users/Ananya/Desktop/major_prjct/Test/n/lungn16.jpeg',
    # 'C:/path_to_your_image2.jpg',
    # Add more image paths as needed
]


# Predict and display results for each image
for img_path in image_paths:
    predict_and_display(img_path, img_height, img_width)
