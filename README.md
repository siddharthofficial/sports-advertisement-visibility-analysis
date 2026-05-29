# Paytm Advertisement Visibility Analytics using YOLOv8 & Faster R-CNN

## Project Overview

This project develops an end-to-end Computer Vision pipeline to measure the effectiveness of Paytm's stadium advertisements during cricket broadcasts.

The system automatically detects Paytm logos from match footage, classifies their visibility, quantifies advertisement exposure, and generates actionable business insights.

The project was developed as a Machine Learning Engineering use case focused on real-world advertisement analytics and sports broadcasting intelligence.


## Business Problem

Paytm invests heavily in cricket sponsorships and stadium advertisements. However, advertisement effectiveness depends on how frequently and how clearly the logo appears during televised broadcasts.

Manually reviewing hours of match footage is time-consuming, expensive, and error-prone.

This project automates the entire process by:

* Detecting Paytm logos from broadcast footage
* Classifying visibility levels
* Measuring advertisement exposure time
* Generating visibility analytics
* Providing business recommendations for future ad placements


## Objectives

### Logo Detection

Identify Paytm logos in cricket broadcast frames.

### Visibility Classification

Classify detections into:

* Fully Visible
* Partially Visible
* Not Visible

### Exposure Analytics

Generate:

* Total exposure duration
* Visibility percentage
* Appearance frequency
* Frame-level analytics
* Timeline reports

### Business Intelligence

Provide data-driven insights about advertisement effectiveness and camera coverage patterns.


## Dataset

The dataset was created using cricket broadcast footage and manually annotated logo bounding boxes.

### Classes

| Class ID | Label                  |
| -------- | ---------------------- |
| 0        | Fully Visible Logo     |
| 1        | Partially Visible Logo |

The repository includes representative samples from:

* Training Dataset
* Validation Dataset
* Test Dataset



## Methodology

Instead of directly choosing a model, multiple object detection architectures were evaluated.

### Model 1: Faster R-CNN

Implemented Faster R-CNN with ResNet50-FPN backbone using PyTorch.

Training Features:

* Transfer Learning
* Mixed Precision Training
* Early Stopping
* Validation Monitoring

### Model 2: YOLOv8

Implemented YOLOv8 for real-time logo detection.

Training Configuration:

* Image Size: 512×512
* Epochs: 30
* Batch Size: 16
* Transfer Learning from Pretrained Weights



## Model Comparison

| Metric                 | YOLOv8    | Faster R-CNN |
| ---------------------- | --------- | ------------ |
| mAP@0.5                | 0.904     | 0.225        |
| FPS                    | 120       | 10.88        |
| Recall                 | 0.857     | 0.914        |
| Deployment Suitability | Excellent | Moderate     |

### Final Model Selection

YOLOv8 was selected as the production model because it achieved:

* 4x higher detection accuracy
* More than 11x faster inference
* Better suitability for real-time deployment
* Superior scalability for live broadcast analytics



## Video Analytics Pipeline

The trained YOLOv8 model processes cricket match footage frame-by-frame.

Pipeline:

1. Video Input
2. Frame Extraction
3. Logo Detection
4. Visibility Classification
5. Exposure Measurement
6. Timeline Generation
7. Dashboard Reporting



## Advertisement Exposure Results

### Broadcast Analysis

| Metric                   | Value     |
| ------------------------ | --------- |
| Total Frames Analyzed    | 14,454    |
| Fully Visible Frames     | 1,225     |
| Partially Visible Frames | 166       |
| No Logo Frames           | 13,063    |
| Fully Visible Time       | 40.83 sec |
| Partially Visible Time   | 5.53 sec  |
| Total Exposure Time      | 46.37 sec |
| Visibility Rate          | 9.62%     |



## Business Insights

### Advertisement Visibility

Only 9.62% of total broadcast time contained visible Paytm branding.

This indicates that a significant portion of the match footage does not contribute to advertisement exposure.

### Camera Angle Analysis

Spatial heatmap analysis revealed that logo detections were concentrated in specific regions of the broadcast frame.

This suggests that certain camera angles consistently provide stronger advertisement visibility than others.

### Sponsorship Effectiveness

The system enables advertisers to move beyond sponsorship spending and quantitatively measure:

* Advertisement exposure
* Visibility quality
* Broadcast effectiveness
* ROI-related visibility metrics

### Strategic Recommendation

Future sponsorship negotiations can use visibility analytics to:

* Optimize hoarding placement
* Improve camera-facing advertisement positions
* Increase brand exposure frequency



## Dashboard Features

Interactive Streamlit dashboard providing:

* Exposure Metrics
* Visibility Rate
* Appearance Counts
* Frame-wise Analytics
* Timeline Visualization
* CSV Report Export



## Technologies Used

### Machine Learning

* YOLOv8
* Faster R-CNN
* PyTorch
* Ultralytics

### Computer Vision

* OpenCV

### Data Processing

* NumPy
* Pandas

### Visualization

* Matplotlib

### Deployment

* Streamlit



## Repository Structure

```text
paytm-ad-visibility-analytics/
│
├── app.py
├── paytm_logo_visibility_training.ipynb
├── requirements.txt
├── README.md
│
├── train_samples/
├── validation_samples/
├── test_samples/
│
├── screenshots/
│
└── outputs/
```



## Key Skills Demonstrated

* Computer Vision
* Object Detection
* YOLOv8
* Faster R-CNN
* Model Evaluation
* Business Analytics
* Video Processing
* Streamlit Deployment
* Machine Learning Engineering
* Data Visualization
* Sports Analytics


## Author

Siddharth Jain
