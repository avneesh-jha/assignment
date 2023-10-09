from io import StringIO
import cv2
import numpy as np
from PIL import Image
import pandas as pd
import easyocr
import os
import pandas as pd


reader = easyocr.Reader(["en"], gpu=True)
excel_path = "task3/output_data/output_file.xlsx"
image_path = "task3/input_data/image_read.png"
croppped_image_path = r"task3/input_data/cropped_image.png"


def extract_text(path_to_cropped_image):
    extracted_text = reader.readtext(path_to_cropped_image, detail=0)
    return extracted_text


# Load the image and Convert BGR to RGB
try:
    img = cv2.imread(image_path)

except:
    print("no image is present at the given path")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# upper and lower limit red color intensity in RGB
lower_red = np.array([150, 0, 0], dtype=np.uint8)
upper_red = np.array([255, 50, 50], dtype=np.uint8)

# Threshold the image to get a binary mask
mask = cv2.inRange(img_rgb, lower_red, upper_red)

# Find contours in the binary mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    # Get the bounding box of the first contour (assuming it's the red rectangle)
    x, y, w, h = cv2.boundingRect(contours[0])

    # Crop the image
    cropped_image = img[y : y + h, x : x + w]

    Image.fromarray(cropped_image).save(croppped_image_path)

    extracted_text = extract_text(croppped_image_path)
    df = pd.DataFrame(extracted_text)
    df.to_excel(excel_path, index=False)
    print(df)
    if os.path.exists(croppped_image_path):
        # Delete the file
        os.remove(croppped_image_path)
        print(f"File '{croppped_image_path}' deleted successfully.")

else:
    print("No red border box is availbale in the image.")
