# Pear640 Dataset

A dataset of pear fruit images captured in pear orchards, designed for object detection tasks using YOLO architecture.

## Dataset Description

The Pear640 dataset is designed for pear fruit detection tasks. It contains annotated photographs of pear orchards, making it suitable for computer vision, object detection, and deep learning research in agricultural applications.

- **Number of classes**: 1 (Pear fruits)
- **Image format**: YOLO format & COCO-like JSON
- **Image size**: 640x640 pixels

## Dataset Structure

The dataset includes:
- Annotated images (640x640)
- YOLO format annotations
- COCO-like JSON annotations
- Single class annotations for pear fruits

**Directory Example:**
```
data/
  images/
    DSC_1352_12kv2r1k_0.jpg
    DSC_1352_12kv2r1k_0.json
    ...
```

## Database Structure

This dataset does not use a traditional database, but organizes data by files. Each image (.jpg) has a corresponding annotation file (.json), which describes the image and its annotations in a COCO-like structure, suitable for direct use in deep learning training.

- **images/**  
  Stores all images and their corresponding JSON annotation files.
- **Each JSON file**  
  Contains image metadata, annotation information, and category information.

## JSON Structure Explanation

Each JSON file follows a COCO-like structure (one image per file):

```json
{
  "info": {
    "description": "data",
    "version": "1.0",
    "year": 2025,
    "contributor": "search engine",
    "source": "augmented",
    "license": {
      "name": "Creative Commons Attribution 4.0 International",
      "url": "https://creativecommons.org/licenses/by/4.0/"
    }
  },
  "images": [
    {
      "id": 9326712356,
      "width": 640,
      "height": 640,
      "file_name": "DSC_1352_12kv2r1k_0.jpg",
      "size": 68187,
      "format": "JPEG",
      "url": "",
      "hash": "",
      "status": "success"
    }
  ],
  "annotations": [
    {
      "id": 1826122356,
      "image_id": 9326712356,
      "category_id": 5168985379,
      "segmentation": [],
      "area": 1826.12,
      "bbox": [x, y, width, height],
      "iscrowd": 0
    }
    // ... more objects
  ],
  "categories": [
    {
      "id": 5168985379,
      "name": "pear640",
      "supercategory": "pear"
    }
  ]
}
```

- **images**: Image metadata (id, size, filename, etc.)
- **annotations**: Annotation info, one object per dict, including bbox ([x, y, width, height]), area, iscrowd, etc.
- **categories**: Category info (only one class: pear640)

## Applications

This dataset can be used for:
- Pear fruit detection
- Object detection
- Computer vision research
- Deep learning model training
- Agricultural AI applications

## Categories

- Computer Science
- Artificial Intelligence
- Computer Vision
- Object Detection
- Machine Learning
- Agriculture
- Deep Learning
- Precision Agriculture

## Citation

```
Sergejs Kodors, Marks Sondors, Gunārs Lācis, Edgars Rubauskis, Ilmārs Apeināns, Imants Zarembo. "RAPID PROTOTYPING OF PEAR DETECTION NEURAL NETWORK WITH YOLO ARCHITECTURE IN PHOTOGRAPHS," In Proceedings of the International Scientific and Practical Conference "Environment. Technology. Resources.", Rezekne, Latvia, June 15-16, 2023, vol. 1, pp. 81-85, doi: 10.17770/etr2023vol1.7293
```

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Source

The dataset is available at:
- [Kaggle Dataset](https://www.kaggle.com/datasets/projectlzp201910094/pear640)
- [Papers with Code](https://paperswithcode.com/dataset/pear640) 