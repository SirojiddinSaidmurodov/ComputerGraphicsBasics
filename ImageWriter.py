from threading import Thread
import cv2 as cv


class ImageWriter(Thread):
    def __init__(self, image_mat, name, folder):
        Thread.__init__(self)
        self.name = name
        self.image_mat = image_mat
        self.folder = folder

    def run(self):
        cv.imwrite(self.folder + "\\" + self.name + ".jpg", self.image_mat)
