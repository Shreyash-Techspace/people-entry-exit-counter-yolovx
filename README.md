# People Entry Exit Counter using YOLOvX

## Overview

This project is a real-time People Entry and Exit Counter developed using YOLOvX and Computer Vision techniques. The system detects and tracks people entering and exiting through a defined region using webcam or video input.

The project focuses on accurate real-time human detection and counting with efficient performance and high detection accuracy.

---

## Demo Video 
[Watch Project Demo](https://drive.google.com/file/d/192rZVHiZvv4twVxG90PZLGhgTeWnOHdp/view?usp=sharing)

## Features

* Real-time people detection
* Entry and Exit counting
* YOLOvX based object detection
* Webcam and video support
* High detection accuracy
* Lightweight and efficient implementation

---

## Technologies Used

* Python
* YOLOvX
* OpenCV
* NumPy
* Google Colab
* VS Code

---

## Project Workflow

1. Dataset Collection
2. Data Annotation
3. Data Augmentation
4. Model Training using YOLOvX
5. Real-time Detection
6. Entry and Exit Counting
7. Result Analysis

---

## Results

| Metric    | Score  |
| --------- | ------ |
| Precision | 95.04% |
| Recall    | 92.30% |
| mAP       | 95.80% |

---

## Dataset

The annotated and augmented dataset in YOLOv8 format used for training and testing is available below:

[Download Dataset](https://drive.google.com/file/d/16fW-V8cCZak-6AfCryIb7kXuQlrWJvwD/view?usp=drive_link)

---

## Roboflow Dataset

The dataset used for training and augmentation was managed using Roboflow.

[View Roboflow Dataset](https://universe.roboflow.com/shreyashs-workspace-zijct/entry-exit-counting-fz9gk)

---

## Project Structure

```bash id="0n7p2d"
people-entry-exit-counter-yolovx
│
├── app.py
├── Entry_Exit_Counter.ipynb
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

---

## Installation and Execution

### Step 1 — Clone Repository

```bash id="r7g8s2"
git clone https://github.com/Shreyash-Techspace/people-entry-exit-counter-yolovx.git
```

### Step 2 — Open Project Folder

```bash id="q8t5m1"
cd people-entry-exit-counter-yolovx
```

### Step 3 — Install Dependencies

```bash id="k6u3v9"
pip install -r requirements.txt
```

### Step 4 — Run the Project

```bash id="z2x6c1"
python app.py
```

---

## Requirements

```text id="v3b7n5"
opencv-python
numpy
torch
ultralytics
```

---

## Applications

* Smart Surveillance Systems
* Crowd Monitoring
* Office Attendance Monitoring
* Shopping Mall Analytics
* College and Institution Monitoring

---

## Future Scope

* Multi-camera support
* Cloud dashboard integration
* Live analytics system
* Mobile application integration
* Database connectivity

---

## Developed By

Shreyash Bhoir 

---
