import argparse
import os
import cv2
from io_and_transform import load_image, to_gray, resize_keep_aspect, rotate
from enhancement_and_filter import hist_equalize_gray, contrast_stretch, gaussian_blur, sharpen, psnr
from feature_and_edges import canny_edges, hough_lines
from utils import ensure_dir, write_summary

def run(input_path, outdir, show=False, rotate_angle=0):
    ensure_dir(outdir)
    img = load_image(input_path)
    img = resize_keep_aspect(img, width=800)
    if rotate_angle != 0:
        img = rotate(img, rotate_angle)

    gray = to_gray(img)

    he = hist_equalize_gray(gray)
    cs = contrast_stretch(gray)
    blur = gaussian_blur(gray, k=5)
    sharp = sharpen(gray)

    edges = canny_edges(sharp)
    hough = hough_lines(edges, img)

    cv2.imwrite(os.path.join(outdir,'gray.png'), gray)
    cv2.imwrite(os.path.join(outdir,'hist_equalized.png'), he)
    cv2.imwrite(os.path.join(outdir,'contrast_stretch.png'), cs)
    cv2.imwrite(os.path.join(outdir,'blur.png'), blur)
    cv2.imwrite(os.path.join(outdir,'sharpen.png'), sharp)
    cv2.imwrite(os.path.join(outdir,'edges.png'), edges)
    cv2.imwrite(os.path.join(outdir,'hough.png'), hough)

    metrics = {
        'psnr_sharp_vs_gray': psnr(sharp, gray),
        'psnr_blur_vs_gray': psnr(blur, gray)
    }

    write_summary(outdir, {
        'input': input_path,
        'outputs': sorted([f for f in os.listdir(outdir) if not f.startswith('.')]),
        'metrics': metrics
    })

    if show:
        cv2.imshow('Original', img)
        cv2.imshow('Edges', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if _name_ == '_main_':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to input image')
    parser.add_argument('--outdir', default='results', help='Output directory')
    parser.add_argument('--show', action='store_true', help='Show images interactively')
    parser.add_argument('--rotate', type=float, default=0.0, help='Rotate input by degrees (optional)')
    args = parser.parse_args()
    run(args.input, args.outdir, show=args.show, rotate_angle=args.rotate)
