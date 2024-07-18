import numpy as np
import cv2
import imageio
import rembg


class Remover:
    def __init__(self, img_path):
        self.img_path = img_path
        self.image = self.__import_image()

    def __import_image(self):
        return imageio.imread(self.img_path)
    
    def image_wo_background(self):
        return rembg.remove(self.image)