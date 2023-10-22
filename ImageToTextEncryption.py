import numpy as np
from PIL import Image
from EncryptionDecryptionAlgorithm import AESCipher

class ImageEncryptor:
    def __init__(self, key):
        self.key = key

    def encrypt_image(self, image_path):
        image = Image.open(image_path)
        image_array = np.array(image)

        rows, cols = image_array.shape[0], image_array.shape[1]
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
    encrypted_image = encryptor.encrypt_image('encrypted_image_from_image.png')
    with open('encrypted_text.txt', 'w') as f:
        f.write(encrypted_image)

if __name__ == "__main__":
    main()
