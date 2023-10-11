import numpy as np
from PIL import Image

def encryption(image_path):
    
    image = Image.open(image_path)
    
    resize_image = image.resize((5, 5))
    resize_image.save('resized_image.jpg')

    image = Image.open('resized_image.jpg')
    image_array = np.array(image)

    red_channel = image_array[:, :, 0]
    green_channel = image_array[:, :, 1]
    blue_channel = image_array[:, :, 2]

    # print(red_channel)
    # print(green_channel)
    # print(blue_channel)

    array = []
    text = ""
    for i in range(len(red_channel)):
        for j in range(3):
            for k in range(len(red_channel[0])):
                text += str(j) + str(image_array[i][k][j]) + str(i) + str(k) + " "
                array.append(j)
                array.append(image_array[i][k][j])
                array.append(i)
                array.append(k)
            
    return text
    # print(text)
    # print(array)

encryption('image1.jpg')

