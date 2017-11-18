import cv2
import glob
import sys
import os


def main():
  sourceFolder = sys.argv[1]
  sourceFolder += '/*'
  rate = float(sys.argv[2])

  for filename in glob.glob(sourceFolder):
    image = cv2.imread(filename)
    # cv2.imshow(filename + 'raw', image)
    lightenedImage = image * rate
    # cv2.imshow(filename + 'lightened', lightenedImage)
    # lightenedImage = image.convertTo(-1, 2, 0)
    cv2.imshow(filename + 'lightened', lightenedImage)
    newFilename = "result/" + os.path.basename(filename)
    print newFilename
    cv2.imwrite(newFilename, lightenedImage)
    
  cv2.waitKey(0)
  cv2.destroyAllWindows()

main()