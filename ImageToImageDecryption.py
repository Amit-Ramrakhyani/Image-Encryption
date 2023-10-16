from PIL import Image
import numpy as np
import random
from math import log
from EncryptionDecryptionAlgorithm import ArnoldCat

class ImageDecryptor:
    def __init__(self, key):
        self.key = key
        
    def decrypt(self, image):
        arnoldcatdecrypt = ArnoldCat(self.key)
        img = arnoldcatdecrypt.ArnoldCatDecryption(image)
        return img
    
def main():
    key = 100
    decryptor = ImageDecryptor(key)
    img = decryptor.decrypt('encrypted_image.jpg')
    img = Image.fromarray(img)
    img.save('decrypted_image_from_image.jpg')
    
if __name__ == '__main__':
    main()