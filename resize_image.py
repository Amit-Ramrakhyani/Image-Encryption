from PIL import Image

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    resized_image.save('./data/resized_image.png')
    return './data/resized_image.png'

# if __name__ == '__main__':
#     image_path = input('Enter image path: ')
#     height = int(input('Enter height: '))
#     width = int(input('Enter width: '))
#     resize_image(image_path, width, height)

def main(img):
    imagePath = resize_image(img, 1000, 1000)
    return imagePath