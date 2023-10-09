Medical Data Management 101

When working with medical data encountering dicoms is inevitable. In this problem we want to extract and store the data present inside this widely used data modality in a structured manner.

You are provided with some dicom files containing chest x-rays examination records. These records contain imaging and accompanying metadata.
Your task is to extract data from these dicoms using python scripts to the below mentioned formats.

    a) Extract the images from the dicoms into a folder with a suitable name for each extracted image. Note – The extracted image should look visually similar to the dicom image. You can use a suitable dicom viewer to view the images (Home Page - Horos Project, MicroDicom - Free DICOM viewer and software etc.)
    b) Design a suitable class(es) and store the image and other metadata into the class objects. Explain the design choices in the report
    c) Export the extracted metadata into suitably structured Json.

SOLUTION:
Developed Python script that processes DICOM (Digital Imaging and Communications in
Medicine) files. It extracts metadata and converts the pixel data of DICOM images into a visually
simplified form, saving the result as a PNG image. Additionally, it exports the metadata of each
DICOM file to a separate JSON file.


![Alt text]([image link](https://github.com/avneesh-jha/assignment/blob/main/Raw_data/Task-1_flow_chart-1.png)https://github.com/avneesh-jha/assignment/blob/main/Raw_data/Task-1_flow_chart-1.png)
