import numpy as np
from PIL import Image
from EncryptionAlgorithm import AESCipher

def encryption(image_path):
    
    image = Image.open(image_path)
    
    resize_image = image.resize((1000, 1000))
    resize_image.save('resized_image.jpg')

    image = Image.open('resized_image.jpg')
    image_array = np.array(image)

    # red_channel = image_array[:, :, 0]
    # green_channel = image_array[:, :, 1]
    # blue_channel = image_array[:, :, 2]

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
                
    cipher = AESCipher('1f6332526198f90e0b21b831948772ce')
    encrypted = cipher.encrypt(text)            
    return encrypted

def main():
    return encryption('image1.jpg')


