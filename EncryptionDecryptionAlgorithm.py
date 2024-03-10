import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from PIL import Image
import cv2
import numpy as np
import random
from math import log

class AESCipher(object):
    
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
        
    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text
    
    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]
    
    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")
    
    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)


class ArnoldCat:
    def __init__(self, key):
        self.key = key

    def ArnoldCatTransform(self, image, num):
        rows, cols, color_channels = image.shape
        n = rows
        image_arnold = np.zeros([rows, cols, color_channels], dtype=np.uint8)
        
        for x in range(0, rows):
            for y in range(0, cols):
                image_arnold[x][y] = image[(x+y)%n][(x+2*y)%n]
        return image_arnold
    
    def ArnoldCatEncryption(self, imageName):
        img = cv2.imread(imageName)
        for i in range (0, self.key):
            img = self.ArnoldCatTransform(img, i)
        return img
    
    def ArnoldCatDecryption(self, imageName):
        img = cv2.imread(imageName)
        rows, cols, color_channels = img.shape
        dimension = rows
        decrypt_iteration = dimension
        
        if (dimension%2 == 0) and 5**int(round(log(dimension/2, 5))) == int(dimension/2):
            decrypt_iteration = 3 * dimension
        elif 5**int(round(log(dimension, 5))) == int(dimension):
            decrypt_iteration = 2 * dimension
        elif (dimension%6 == 0) and 5**int(round(log(dimension/6, 5))) == int(dimension/6):
            decrypt_iteration = 2 * dimension
        else:
            decrypt_iteration = int(12 * dimension / 7)
        
        for i in range(self.key, decrypt_iteration):
            img = self.ArnoldCatTransform(img, i)
            
        return img
    
class LogisticMap:
    def __init__(self, seed):
        self.seed = seed
    
    def logistic_map(self, x, r):
        return r * x * (1 - x)
    
    def generate_key(self, n):
        key_array = [0] * n
        x = self.seed
        r = 3.6 # Can change the parameter 'r' for different chaotic behavior
        for i in range(n):
            x = self.logistic_map(x, r)  
            key_array[i] = int(x * 255)  # Scale to 0-255

        return key_array
            
    def encrypt_image(self, input_image_path, key):
        image = Image.open(input_image_path)
        image_array = np.array(image)
        
        if len(key) < image_array.size:
            raise ValueError("Key size is too small for the image size.")

        encrypted_image = image_array.copy()
        height, width, channels = image_array.shape

        for i in range(height):
            for j in range(width):
                for channel in range(channels):
                    pixel_value = encrypted_image[i, j, channel]
                    encrypted_pixel = pixel_value ^ int(key[i * width + j])
                    encrypted_image[i, j, channel] = int(encrypted_pixel)

        encrypted_image = Image.fromarray(encrypted_image)
        return encrypted_image
        
    def decrypt_image(self, encrypted_image_path, key):
        encrypted_image = Image.open(encrypted_image_path)
        encrypted_image_array = np.array(encrypted_image)

        decrypted_image = encrypted_image_array.copy()
        height, width, channels = encrypted_image_array.shape

        for i in range(height):
            for j in range(width):
                for channel in range(channels):
                    encrypted_pixel_value = encrypted_image_array[i, j, channel]
                    decrypted_pixel = encrypted_pixel_value ^ key[i * width + j]
                    decrypted_image[i, j, channel] = int(decrypted_pixel)

        decrypted_image = Image.fromarray(decrypted_image)
        return decrypted_image