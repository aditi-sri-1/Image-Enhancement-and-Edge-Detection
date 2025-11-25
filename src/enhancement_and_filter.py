import cv2
import numpy as np

"""Histogram and filtering operations."""

def hist_equalize_gray(gray):
    return cv2.equalizeHist(gray)

def contrast_stretch(gray):
    a, b = int(gray.min()), int(gray.max())
    if b == a:
        return gray.copy()
    stretched = ((gray - a) * (255.0 / (b - a))).astype('uint8')
    return stretched

def gaussian_blur(gray, k=5):
    if k % 2 == 0:
        k += 1
    return cv2.GaussianBlur(gray, (k,k), 0)

def sharpen(gray):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    return cv2.filter2D(gray, -1, kernel)

def psnr(a, b):
    mse = np.mean((a.astype('float64') - b.astype('float64'))**2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))
