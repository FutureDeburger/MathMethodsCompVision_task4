import cv2 as cv
import numpy as np

def detect_pupils(image):

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    inv = 255 - gray

    ksize = 21
    lap = cv.Laplacian(inv, ddepth=cv.CV_32F, ksize=ksize)
    lap_abs = np.abs(lap).astype(np.uint8)

    lap_norm = cv.normalize(lap_abs, None, 0, 255, cv.NORM_MINMAX)

    _, th = cv.threshold(lap_norm, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # cv.imshow("Gray", gray)
    cv.imshow("Inverted", inv)
    # cv.imshow("Laplacian", lap_norm)
    # cv.imshow("Threshold", th)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return th


my_image = cv.imread('face.jpg')
cv.imshow('Image', my_image)

detect_pupils(my_image)