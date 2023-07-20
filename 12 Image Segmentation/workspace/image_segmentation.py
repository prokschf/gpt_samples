import argparse
import requests
from PIL import Image
import torch
from torchvision import models, transforms
import io

# Mapping from COCO category IDs to names
# This is a subset of the full mapping, containing only the categories the model was trained on
COCO_CATEGORIES = {
    0: 'background',
    1: 'person',
    2: 'bicycle',
    3: 'car',
    4: 'motorcycle',
    5: 'airplane',
    6: 'bus',
    7: 'train',
    8: 'truck',
    9: 'boat',
    10: 'traffic light',
    11: 'fire hydrant',
    13: 'stop sign',
    14: 'parking meter',
    15: 'bench',
    16: 'bird',
    17: 'cat',
    18: 'dog',
    19: 'horse',
    20: 'sheep',
    21: 'cow',
    22: 'elephant',
    23: 'bear',
    24: 'zebra',
    25: 'giraffe',
    27: 'backpack',
    28: 'umbrella',
    31: 'handbag',
    32: 'tie',
    33: 'suitcase',
    34: 'frisbee',
    35: 'skis',
    36: 'snowboard',
    37: 'sports ball',
    38: 'kite',
    39: 'baseball bat',
    40: 'baseball glove',
    41: 'skateboard',
    42: 'surfboard',
    43: 'tennis racket',
    44: 'bottle',
    46: 'wine glass',
    47: 'cup',
    48: 'fork',
    49: 'knife',
    50: 'spoon',
    51: 'bowl',
    52: 'banana',
    53: 'apple',
    54: 'sandwich',
    55: 'orange',
    56: 'broccoli',
    57: 'carrot',
    58: 'hot dog',
    59: 'pizza',
    60: 'donut',
    61: 'cake',
    62: 'chair',
    63: 'couch',
    64: 'potted plant',
    65: 'bed',
    67: 'dining table',
    70: 'toilet',
    72: 'tv',
    73: 'laptop',
    74: 'mouse',
    75: 'remote',
    76: 'keyboard',
    77: 'cell phone',
    78: 'microwave',
    79: 'oven',
    80: 'toaster',
    81: 'sink',
    82: 'refrigerator',
    84: 'book',
    85: 'clock',
    86: 'vase',
    87: 'scissors',
    88: 'teddy bear',
    89: 'hair drier',
    90: 'toothbrush',
}

def download_image(url: str) -> Image:
    """Download an image from a URL and return a PIL Image object."""
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(io.BytesIO(response.content))

def segment_image(image: Image) -> list[str]:
    """Segment an image using a pre-trained DeepLabV3 model and return a list of objects in the image."""
    # Load the pre-trained model
    model = models.segmentation.deeplabv3_resnet101(pretrained=True)
    model.eval()

    # Transform the image
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)

    # Run the image through the model
    with torch.no_grad():
        output = model(input_batch)['out'][0]
    output_predictions = output.argmax(0)

    # Identify the objects in the image
    objects = set()
    for category_id in output_predictions.unique().tolist():
        if category_id in COCO_CATEGORIES:
            objects.add(COCO_CATEGORIES[category_id])

    return list(objects)

def main():
    """Handle command line arguments, call the other functions, and print the output."""
    parser = argparse.ArgumentParser(description='Segment an image and identify the objects in it.')
    parser.add_argument('url', help='The URL of the image to segment.')
    args = parser.parse_args()

    image = download_image(args.url)
    objects = segment_image(image)

    print(objects)

if __name__ == '__main__':
    main()
