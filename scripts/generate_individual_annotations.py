import os
import json
import random
import time
from pathlib import Path
import glob

def generate_unique_id():
    """Generate 10-digit random code with last 3 digits as timestamp"""
    # Generate 7 random digits
    random_part = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    # Get last 3 digits of current timestamp
    timestamp_part = str(int(time.time()))[-3:]
    return random_part + timestamp_part

def yolo_to_coco_bbox(yolo_bbox, img_width, img_height):
    """Convert YOLO format bounding box to COCO format"""
    x_center, y_center, width, height = yolo_bbox
    
    # Convert to absolute coordinates
    x_center *= img_width
    y_center *= img_height
    width *= img_width
    height *= img_height
    
    # Convert to COCO format [x, y, width, height]
    x = x_center - width / 2
    y = y_center - height / 2
    
    return [x, y, width, height]

def create_coco_annotation(image_id, annotation_id, category_id, bbox, area):
    """Create COCO format annotation"""
    return {
        "id": annotation_id,
        "image_id": image_id,
        "category_id": category_id,
        "segmentation": [],
        "area": area,
        "bbox": bbox,
        "iscrowd": 0
    }

def process_image_annotations(image_path, label_path, image_id, category_id):
    """Process annotations for a single image"""
    # Get image dimensions (assumed 640x640, adjust as needed)
    img_width, img_height = 640, 640
    
    annotations = []
    annotation_id = int(generate_unique_id())
    
    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) == 5:
                    class_id = int(parts[0])
                    x_center = float(parts[1])
                    y_center = float(parts[2])
                    width = float(parts[3])
                    height = float(parts[4])
                    
                    # Convert to COCO format
                    bbox = yolo_to_coco_bbox([x_center, y_center, width, height], img_width, img_height)
                    area = bbox[2] * bbox[3]  # width * height
                    
                    annotation = create_coco_annotation(image_id, annotation_id, category_id, bbox, area)
                    annotations.append(annotation)
                    annotation_id += 1
    
    return annotations

def create_coco_json(image_path, annotations, image_id, category_id):
    """Create COCO format JSON file"""
    # Get image filename without extension
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    
    # Create COCO format data structure
    coco_data = {
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
                "id": image_id,
                "width": 640,
                "height": 640,
                "file_name": os.path.basename(image_path),
                "size": os.path.getsize(image_path),
                "format": "JPEG",
                "url": "",
                "hash": "",
                "status": "success"
            }
        ],
        "annotations": annotations,
        "categories": [
            {
                "id": category_id,
                "name": "pear640",
                "supercategory": "pear"
            }
        ]
    }
    
    return coco_data

def main():
    # Set paths
    images_dir = "data/images"
    labels_dir = "data/labels"
    
    # Get all image files
    image_files = glob.glob(os.path.join(images_dir, "*.jpg"))
    
    print(f"Found {len(image_files)} images")
    
    for image_path in image_files:
        # Get corresponding label file path
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        label_path = os.path.join(labels_dir, f"{image_name}.txt")
        
        # Generate unique ID
        image_id = int(generate_unique_id())
        category_id = 5168985379  # Use category_id from example
        
        # Process annotations
        annotations = process_image_annotations(image_path, label_path, image_id, category_id)
        
        # Create COCO format JSON data
        coco_data = create_coco_json(image_path, annotations, image_id, category_id)
        
        # Generate JSON filename (using image name)
        json_filename = f"{image_name}.json"
        json_path = os.path.join(os.path.dirname(image_path), json_filename)
        
        # Save JSON file
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(coco_data, f, indent=2, ensure_ascii=False)
        
        print(f"Generated: {json_filename} (contains {len(annotations)} annotations)")

if __name__ == "__main__":
    main() 