from PIL import Image
import numpy as np
import random
from math import log
from EncryptionDecryptionAlgorithm import ArnoldCat

class ImageEncryptor:
    def __init__(self, key):
        self.key = key
        
    def encrypt(self, image):
        arnoldcatencrypt = ArnoldCat(self.key)
        img = arnoldcatencrypt.ArnoldCatEncryption(image)
        return img
    
def main():
    key = 10
    encryptor = ImageEncryptor(key)
    img = encryptor.encrypt('resized_image.jpg')
    img = Image.fromarray(img)
    img.save('encrypted_image.jpg')
    
if __name__ == '__main__':
    main()