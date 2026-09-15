# Step 1: Install required libraries
!pip install -q transformers torch pillow

# Step 2: Import libraries
import os
from PIL import Image
from transformers import pipeline
from google.colab import files

# Step 3: Upload image
print("Please upload an image...")
uploaded = files.upload()

# Get uploaded image name automatically
image_path = list(uploaded.keys())[0]

print("\nImage uploaded:", image_path)

# Step 4: Open image
image = Image.open(image_path).convert("RGB")

print("Image loaded successfully!")

# Step 5: Load AI image classification model
print("\nLoading AI model...")

classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

print("AI model loaded successfully!")

# Step 6: Recognize the image
print("\nRecognizing image...")

results = classifier(image)

# Step 7: Display results
print("\n" + "=" * 50)
print("       IMAGE RECOGNITION RESULT")
print("=" * 50)

for i, result in enumerate(results[:5], start=1):
    label = result["label"]
    score = result["score"] * 100

    print(f"{i}. {label} - {score:.2f}%")

print("=" * 50)
print("Image recognition completed successfully!")