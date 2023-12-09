YOLO Traffic Sign Detection for UAV Applications
Introduction

This GitHub repository contains the implementation of an effective and efficient traffic sign detection system for Unmanned Aerial Vehicles (UAVs) using the You Only Look Once (YOLO) detection framework. The project explores the integration of machine learning and object detection technologies to enhance the capabilities of UAVs in various applications, such as agriculture, infrastructure monitoring, and disaster response.
Project Details

    Author: Joel Mendez
    Supervisor: Brent Horine
    Date: 12/08/2023

Project Overview

In recent years, the YOLO framework has gained prominence in real-time object detection, making it particularly suitable for UAVs where quick decision-making is essential. The primary goal of this project was to leverage YOLO for traffic sign detection in UAV applications, delving into methodologies, challenges, and key learnings associated with the development process.
Methodologies and Discussions
Setting Up YOLOv8

Before training, it is crucial to set up the environment with the necessary dependencies. A virtual environment using Anaconda was created, and all dependencies are listed in the requirements.txt file.
Dataset Collection and Preprocessing

The project involved merging pre-labeled datasets and creating a custom dataset. Open-source tools like Universe Roboflow were employed for dataset acquisition. Python scripts (merge.py and count.py) facilitated dataset customization, while the labelImg software was used for custom labeling.
Model Training

The YOLOv8 model was trained using a split dataset for training and validation. The Optuna library was employed for hyperparameter optimization to enhance model performance. The training process involved selecting a pre-trained model from the Ultralytics GitHub repository and utilizing CUDA technology for faster training.
Model Evaluation

Various performance metrics, including F1-Confidence Curve, Precision-Confidence Curve, Precision-Recall Curve, Recall-Confidence Curve, Box Loss, and mAP, were used to evaluate the model's accuracy and reliability for traffic sign detection in UAV applications.
Improvements

To enhance the model's functionality, string extraction using the Tesseract library was implemented. Additionally, a web application was developed using Flask, HTML, CSS, and JavaScript to provide an intuitive interface for testing and implementing the project.
Key Learnings and Challenges
Key Learnings

    Training computer vision models for object detection.
    Optimizing machine learning networks using Optuna.
    Data gathering and processing.
    Implementing string extraction algorithms.
    Evaluating models based on performance metrics.
    Exposure to web development.

Challenges

    Dataset acquisition and merging challenges.
    Lengthy training times without CUDA.
    Errors in real-time string extraction.
    Project management challenges due to concurrent tasks.

Conclusion

The project successfully developed a robust traffic sign detection system for UAVs using the YOLO framework. The methodologies employed provided exposure to various technologies, frameworks, and challenges associated with computer vision and machine learning. The project concludes with insights into potential future developments, such as implementing the model on a mini-vehicle for autonomous driving.
References

    Ultralytics GitHub Repository
    Universe Roboflow
    YOLOv8 Documentation
    OpenCV Tutorials
    YouTube: YOLO Object Detection
    YouTube: YOLOv8 Training

For the complete source code and details, please refer to the files in this repository.


