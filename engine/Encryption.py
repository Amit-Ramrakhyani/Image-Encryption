import engine.ImageToImageEncryption as ImageToImageEncryption
import engine.ImageToTextEncryption as ImageToTextEncryption
import engine.resize_image as resize_image

image = './data/image1.jpg'

def main(image):
    resized = resize_image.main(image)
    encrypted_imgpth = ImageToImageEncryption.main(resized)
    ImageToTextEncryption.main(encrypted_imgpth)
    
if __name__ == '__main__':
    main()
    