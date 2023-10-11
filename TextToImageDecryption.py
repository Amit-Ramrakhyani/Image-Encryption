import numpy as np
from PIL import Image
from EncryptionAlgorithm import AESCipher
import math
import ImageToTextEncryption as itte

def decryption(cipher_text):
    
    cipher = AESCipher('1f6332526198f90e0b21b831948772ce')
    decrypted = cipher.decrypt(cipher_text)            
    decrypted = str(decrypted)
    
    array = decrypted.split(" ")
    array.pop()
    # print(array)
    
    cols = rows = int(math.sqrt(len(array)/3))
    print(rows, cols)
    image_array = np.zeros((rows, cols, 3), dtype=np.uint8)
    
    array_index = 0
    for i in range(rows):
        for j in range(3):
            for k in range(cols):
                row = int(array[array_index][(len(array[array_index]) - (len(str(i)) + len(str(k)))):(len(array[array_index]) - len(str(k)))])
                col = int(array[array_index][(len(array[array_index]) - len(str(k))):])
                color_channel = int(array[array_index][0])
                # print("Row: ", row, "i: ", i, "Col: ", col, "k: ", k)
                # print("Color Channel: ", array[array_index][0], "j: ", j)
                array[array_index] = array[array_index][1:]
                array[array_index] = array[array_index][:len(array[array_index]) - (len(str(i)) + len(str(k)))]
                image_array[row][col][color_channel] = array[array_index]
                array_index += 1
                
    print(image_array)
    image = Image.fromarray(image_array)
    image.save('decrypted_image.jpg')
    # image = Image.open(image_path)    
    # resize_image = image.resize((5, 5))
    # resize_image.save('resized_image.jpg')

    # image = Image.open('resized_image.jpg')
    # image_array = np.array(image)

    # red_channel = image_array[:, :, 0]
    # green_channel = image_array[:, :, 1]
    # blue_channel = image_array[:, :, 2]

    # array = []
    # text = ""
    # for i in range(len(image_array[:, :, 0])):
    #     for j in range(3):
    #         for k in range(len(image_array[:, :, 0])):
    #             text += str(j) + str(image_array[i][k][j]) + str(i) + str(k) + " "
    #             array.append(j)
    #             array.append(image_array[i][k][j])
    #             array.append(i)
    #             array.append(k)
                
    # cipher = AESCipher('1f6332526198f90e0b21b831948772ce')
    # encrypted = cipher.encrypt(text)            
    # return encrypted



cipher_text = itte.main()
print(decryption(cipher_text))


