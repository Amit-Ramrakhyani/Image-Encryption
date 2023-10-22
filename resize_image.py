from PIL import Image

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    resized_image.save('resized_image.png')
    return 'resized_image.jpg'

if __name__ == '__main__':
    image_path = input('Enter image path: ')
    height = int(input('Enter height: '))
    width = int(input('Enter width: '))
    resize_image(image_path, width, height)