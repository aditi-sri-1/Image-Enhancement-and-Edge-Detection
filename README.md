# Image-Enhancement-and-Edge-Detection
Computer Vision Project
# ImageEnhance-and-Edges

Tiny beginner CV project: image enhancement + edge detection — designed to meet course project grading criteria.

*Reference guideline:* /mnt/data/project-vityarthi.pdf

## What it does
- Loads an image, resizes, and optionally rotates.
- Performs histogram equalization and contrast stretching.
- Applies Gaussian blur and sharpening (convolution).
- Detects edges using Canny and overlays Hough lines.
- Saves outputs and produces a summary JSON (PSNR metrics included).

## Install (macOS/Linux)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
