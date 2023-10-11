import numpy as np
from PIL import Image
from EncryptionAlgorithm import AESCipher
import math
import ImageToTextEncryption as itte

class ImageDecryptor:
    def __init__(self, key):
        self.key = key

    def decrypt_image(self, cipher_text):
        cipher = AESCipher(self.key)
        decrypted = cipher.decrypt(cipher_text)
        decrypted = str(decrypted)

        array = decrypted.split(" ")
        array.pop()

        cols = rows = int(math.sqrt(len(array) / 3))
        print(rows, cols)
        image_array = np.zeros((rows, cols, 3), dtype=np.uint8)

        array_index = 0
        for i in range(rows):
            for j in range(3):
                for k in range(cols):
                    row = int(array[array_index][(len(array[array_index]) - (len(str(i)) + len(str(k)))):(len(array[array_index]) - len(str(k)))])
                    col = int(array[array_index][(len(array[array_index]) - len(str(k))):])
                    color_channel = int(array[array_index][0])
                    array[array_index] = array[array_index][1:]
                    array[array_index] = array[array_index][:len(array[array_index]) - (len(str(i)) + len(str(k)))]
                    image_array[row][col][color_channel] = array[array_index]
                    array_index += 1

        print(image_array)
        image = Image.fromarray(image_array)
        image.save('decrypted_image.jpg')

def main():
    key = '1f6332526198f90e0b21b831948772ce'
    encryptor = itte.ImageEncryptor(key)
    cipher_text = itte.main()
    
    decryptor = ImageDecryptor(key)
    decryptor.decrypt_image(cipher_text)

if __name__ == "__main__":
    main()
