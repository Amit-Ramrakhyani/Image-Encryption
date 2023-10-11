import numpy as np
from PIL import Image
from EncryptionAlgorithm import AESCipher

class ImageEncryptor:
    def __init__(self, key):
        self.key = key

    def resize_image(self, image_path, width=1000, height=1000):
        image = Image.open(image_path)
        resized_image = image.resize((width, height))
        resized_image.save('resized_image.jpg')
        return 'resized_image.jpg'

    def encrypt_image(self, image_path):
        resized_image_path = self.resize_image(image_path)
        image = Image.open(resized_image_path)
        image_array = np.array(image)

        rows = cols = len(image_array[:, :, 0])
        array = []
        text = ""

        for i in range(rows):
            for j in range(3):
                for k in range(cols):
                    text += str(j) + str(image_array[i][k][j]) + str(i) + str(k) + " "
                    array.append(j)
                    array.append(image_array[i][k][j])
                    array.append(i)
                    array.append(k)

        cipher = AESCipher(self.key)
        encrypted = cipher.encrypt(text)
        return encrypted

def main():
    key = '1f6332526198f90e0b21b831948772ce'
    encryptor = ImageEncryptor(key)
    encrypted_image = encryptor.encrypt_image('image1.jpg')
    return encrypted_image
