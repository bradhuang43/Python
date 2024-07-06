import tensorflow as tf
import numpy as np
import cv2
import pytesseract
from PIL import Image

"""# Open the image file
img = Image.open("C:/Users/giant/Brad/Python/MyOwnProjects/ImageDisplayer/GunnHighSchoolRun.jpg")

# Perform OCR on the image without displaying the progress bar
config = "--psm 3"  # Page segmentation mode
text = pytesseract.image_to_string(img, config = config)

# Save the extracted text to a file
with open("C:/Users/giant/Brad/Python/MyOwnProjects/ImageRecognitionProject/Output.txt", "w") as f:
    f.write(text)

# Alternatively, print a preview of the extracted text
print(text[:10])  # Print the first 10 characters"""

# Load the pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights = "imagenet")

# Function to preprocess the input image
def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Resize the image to 224x224 pixels
    image = cv2.resize(image, (224, 224))
    # Convert the image to a numpy array
    image = np.array(image, dtype = np.float32)
    # Scale the image pixels to the range [0, 1]
    image /= 255.0
    # Expand the dimensions to match the input shape of the model
    image = np.expand_dims(image, axis = 0)
    return image

# Function to make predictions and decode them
def predict_image(image_path):
    # Preprocess the image
    image = preprocess_image(image_path)
    # Make predictions
    predictions = model.predict(image)
    # Decode the predictions to get human-readable labels
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top = 3)
    return decoded_predictions

# Main function to test the model with an image
def main():
    image_path = "Item2.jfif"
    predictions = predict_image(image_path)
    for i, (imagenet_id, label, score) in enumerate(predictions[0]):
        print(f"{i + 1}: {label} ({score:.2f})")

if __name__ == "__main__":
    main()
