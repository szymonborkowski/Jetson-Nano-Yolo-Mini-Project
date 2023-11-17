"""
This script was used to convert the hagrid annotations (coco format) to yolo format.
"""

import json
import os

# dataset: https://github.com/hukenovs/hagrid

# Define a dictionary to map gesture labels to class IDs
gesture_labels = {
    'call': 0,
    'dislike': 1,
    'fist': 2,
    'four': 3,
    'like': 4,
    'mute': 5,
    'ok': 6,
    'one': 7,
    'palm': 8,
    'peace_inverted': 9,
    'peace': 10,
    'rock': 11,
    'stop_inverted': 12,
    'stop': 13,
    'three': 14,
    'three2': 15,
    'two_up_inverted': 16,
    'two_up': 17
}

for label in gesture_labels:

    # Load the JSON file
    json_file = './ann_subsample/' + str(label) + '.json'
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Define a function to convert JSON annotations to YOLO format
    image_ids = []

    def json_to_yolo(data):
        yolo_lines = []
        for image_id, info in data.items():
            image_ids.append(image_id)
            bboxes = info.get("bboxes", [])
            labels = info.get("labels", [])
            landmarks = info.get("landmarks", [])
            leading_hand = info.get("leading_hand", "right")
            leading_conf = info.get("leading_conf", 1.0)
            user_id = info.get("user_id", "default_user_id")

            for i, bbox in enumerate(bboxes):
                x, y, w, h = bbox
                x_center = x + w / 2
                y_center = y + h / 2

                # Map gesture label to class ID
                class_id = gesture_labels.get(labels[i], -1)  # -1 for unknown gestures

                # Change this to the specific gesture I'm looking for?
                if class_id == gesture_labels[label]:
                    yolo_line = f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}"

                    yolo_lines.append(yolo_line)

        return yolo_lines

    # Convert JSON annotations to YOLO format
    yolo_lines = json_to_yolo(data)

    i = 0
    for line in yolo_lines:
        with open('out/' + str(label) + '/' + str(image_ids[i]) + '.txt', 'w') as yolo_file:
            yolo_file.write(line)
        i += 1
