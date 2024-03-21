from PIL import Image
import numpy as np
import random
from math import log
from engine.EncryptionDecryptionAlgorithm import LogisticMap

class ImageEncryptor:
    def __init__(self, seed):
        self.seed = seed
        
    def encrypt(self, image):
        img = Image.open(image)
        img_array = np.array(img)
        n = img_array.shape[0] * img_array.shape[1] * img_array.shape[2]
        
        logisticmap = LogisticMap(self.seed)
        key = logisticmap.generate_key(n)
        encrypted_image = logisticmap.encrypt_image(image, key)
        encrypted_image.save('./data/encrypted_image_from_image.png')
        return './data/encrypted_image_from_image.png'
    
def main(imagePath):
    seed = 0.4
    encryptor = ImageEncryptor(seed)
    return encryptor.encrypt(imagePath)

# if __name__ == '__main__':
#     main()