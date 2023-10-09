import numpy as np
import pydicom
from PIL import Image
import os

import json


class dicomData:
    def __init__(self, image_dicom):
        self.image_dicom = image_dicom
        self.dicom_metadata = {}
        self.simple_image_data = None

    def fetch_metadata(self):
        data = pydicom.filereader.dcmread(self.image_dicom, stop_before_pixels=True)
        self.dicom_metadata = data.to_json_dict()

    def extract_simple_image(self):
        simple_iamge = pydicom.dcmread(self.image_dicom)
        simple_iamge = simple_iamge.pixel_array.astype(float)
        rescaled_image = (np.maximum(simple_iamge, 0) / simple_iamge.max()) * 255
        self.simple_image_data = np.uint8(rescaled_image)
        self.simple_image_data = Image.fromarray(self.simple_image_data)

    def save_image(self, output_folder):
        os.makedirs(output_folder, exist_ok=True)
        image_name = f"{os.path.basename(self.image_dicom).split('/')[-1]}.png"
        image_path = os.path.join(output_folder, image_name)
        self.simple_image_data.save(image_path)

    def export_metadata_to_json(self, output_json):
        with open(
            f"{output_json}/{os.path.basename(self.image_dicom).split('/')[-1]}.json",
            "w",
        ) as json_file:
            json.dump(self.dicom_metadata, json_file, indent=2)
            json_file.write("\n")  # Add a newline between JSON objects


def process_dicom_folder(input_folder, output_folder, json_output_file):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(".dicom"):
                dicom_file_path = os.path.join(root, file)
                dicom_image = dicomData(dicom_file_path)
                dicom_image.fetch_metadata()
                dicom_image.extract_simple_image()
                dicom_image.save_image(output_folder)
                dicom_image.export_metadata_to_json(json_output_file)


input_images_path = "task1/input"
output_images_path = "task1/output"
output_metadata_path = "task1/metadata"


process_dicom_folder(input_images_path, output_images_path, output_metadata_path)
