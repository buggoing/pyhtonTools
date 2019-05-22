import os
import sys
import cv2


def compress2jpg(filepath, quality):
    img = cv2.imread(filepath)
    img = cv2.resize(img, (900, 500))
    filename_ext = os.path.basename(filepath)
    filename, extension = os.path.splitext(filename_ext)
    newFilepath = filename + '_mini.jpg'
    print(newFilepath)
    cv2.imwrite(newFilepath, img, [int(cv2.IMWRITE_JPEG_QUALITY),quality])

print(sys.argv)
compress2jpg(sys.argv[1], 70)