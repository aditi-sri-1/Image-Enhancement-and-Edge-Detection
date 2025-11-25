import cv2
import numpy as np

"""IO and basic transforms."""

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {path}")
    return img

def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def resize_keep_aspect(img, width=800):
    h,w = img.shape[:2]
    if w == width:
        return img
    scale = width / float(w)
    return cv2.resize(img, (width, int(round(h*scale))))

def rotate(img, angle_deg):
    h,w = img.shape[:2]
    M = cv2.getRotationMatrix2D((w/2,h/2), angle_deg, 1.0)
    return cv2.warpAffine(img, M, (w,h))
