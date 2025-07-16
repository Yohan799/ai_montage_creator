# utils/image_ranker.py
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import os

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def rank_images_by_prompt(image_paths, prompt):
    scores = []

    for image_path in image_paths:
        image = Image.open(image_path).convert("RGB")
        inputs = processor(text=[prompt], images=image, return_tensors="pt", padding=True)
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image
        score = logits_per_image[0][0]  # A single scalar tensor
        scores.append(score)

    # 🔧 Convert all scores to Python floats before sorting
    scores = [score.item() for score in scores]

    # Sort images based on scores (higher is better)
    scored_images = sorted(zip(image_paths, scores), key=lambda x: x[1], reverse=True)
    ranked_paths = [path for path, score in scored_images]

    return ranked_paths
