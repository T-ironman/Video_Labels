# -*- encoding=utf-8 -*-
import cv2
import os

def RGB_TO_HSV(img_path):
    images = os.listdir(img_path)
    for image in images:
        image_path = os.path.abspath(os.path.join(img_path,image))
        img_RGB = cv2.imread(image_path, cv2.IMREAD_COLOR)
        img_HSV = cv2.cvtColor(img_RGB,cv2.COLOR_BGR2HSV)
        save_path = os.path.abspath(os.path.join(img_path, 'hsv' + image))
        cv2.imwrite('%s' % save_path, img_HSV)

if __name__ == '__main__':
    RGB_TO_HSV('./img')
