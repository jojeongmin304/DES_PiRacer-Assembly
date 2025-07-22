import cv2
from picamera2 import Picamera2
import time

# Initialize the Picamera2 module
picam2 = Picamera2()

# Configure the camera for still capture
config = picam2.create_still_configuration()
picam2.configure(config)

# Start the camera and allow it to warm up
print("Starting camera...")
picam2.start()
time.sleep(2) # 2-second warm-up

# Capture the image as a NumPy array
# The 'main' stream is used for the full-resolution image
print("Capturing image...")
image = picam2.capture_array("main")

# Stop the camera
picam2.stop()
print("Camera stopped.")

# OpenCV expects BGR format, but Picamera2 captures in RGB.
# Convert the image from RGB to BGR for saving with OpenCV.
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Save the image
try:
    cv2.imwrite('image.png', image_bgr)
    print("Image saved successfully as image.png")
except Exception as e:
    print(f"Error saving image: {e}")

