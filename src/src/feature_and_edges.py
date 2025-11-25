import cv2
import numpy as np

"""Edge detection and Hough lines."""

def canny_edges(gray, low=50, high=150):
    return cv2.Canny(gray, low, high)

def hough_lines(edge_img, orig_img, minLineLength=30, maxLineGap=10, threshold=80):
    lines = cv2.HoughLinesP(edge_img, 1, np.pi/180, threshold=threshold,
                            minLineLength=minLineLength, maxLineGap=maxLineGap)
    out = orig_img.copy()
    if lines is not None:
        for x1,y1,x2,y2 in lines[:,0]:
            cv2.line(out,(x1,y1),(x2,y2),(0,255,0),2)
    return out
