from flask import Flask, request, jsonify, send_file
from transformers import SegformerImageProcessor, AutoModelForSemanticSegmentation
from PIL import Image
import torch.nn as nn
import os
import matplotlib.pyplot as plt
import numpy as np

def process_image(image):
    """Process the image to perform semantic segmentation."""
    processor = SegformerImageProcessor.from_pretrained("sayeed99/segformer-b3-fashion")
    model = AutoModelForSemanticSegmentation.from_pretrained("sayeed99/segformer-b3-fashion")

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits.cpu()

    upsampled_logits = nn.functional.interpolate(
        logits,
        size=image.size[::-1],
        mode="bilinear",
        align_corners=False,
    )

    pred_seg = upsampled_logits.argmax(dim=1)[0].numpy()
    return pred_seg

def save_segmentation_as_image(segmentation, output_path):
    """Save the segmentation map as an image."""
    plt.imshow(segmentation)
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()

app = Flask(__name__)

@app.route("/segment", methods=["POST"])
def segment():
    """API endpoint to segment an image."""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided."}), 400

    file = request.files['file']
    image = Image.open(file.stream)

    try:
        segmentation = process_image(image)
        output_path = "segmentation_output.png"
        save_segmentation_as_image(segmentation, output_path)

        return send_file(output_path, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5001, debug=True)

# curl -X POST -F "file=@segme1.jpg" http://127.0.0.1:5001/segment --output segmented_output.png