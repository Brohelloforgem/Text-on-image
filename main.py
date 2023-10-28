import cv2
import numpy as np
import random

# Load the sunset image
image = cv2.imread("sunset.jpg")

# Read a random text from the "text.txt" file
with open("text.txt", "r") as file:
    lines = file.readlines()
    random_text = random.choice(lines)

# Position to place the text (centered)
text_position = (image.shape[1] // 2 - 150, image.shape[0] // 2)

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
font_color = (0, 0, 255)  # Red color

# Write the text on the image
image_with_text = image.copy()
cv2.putText(image_with_text, random_text, text_position, font, font_scale, font_color, font_thickness)

# Save the image with the added text
cv2.imwrite("sunset_with_text.jpg", image_with_text)

# Display the image
cv2.imshow("Image with Text", image_with_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
