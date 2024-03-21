from PIL import Image
import numpy as np
import random
from math import log
from engine.EncryptionDecryptionAlgorithm import ArnoldCat, LogisticMap

class ImageDecryptor:
    def __init__(self, seed):
        self.seed = seed
        
    def decrypt(self, image):
        img = Image.open(image)
        img_array = np.array(img)
        n = img_array.shape[0] * img_array.shape[1] * img_array.shape[2]
        
        logisticmap = LogisticMap(self.seed)
        key = logisticmap.generate_key(n)
        decrypted_image = logisticmap.decrypt_image(image, key)
        decrypted_image.save('./data/decrypted_image_from_image.png')
    
def main(img):
    seed = 0.4
    decryptor = ImageDecryptor(seed)
    decryptor.decrypt(img)
        
# if __name__ == '__main__':
#     main()