import ImageToImageEncryption
import ImageToTextEncryption
import resize_image

image = './data/image1.jpg'

def main():
    resized = resize_image.main(image)
    encrypted_imgpth = ImageToImageEncryption.main(resized)
    ImageToTextEncryption.main(encrypted_imgpth)
    
if __name__ == '__main__':
    main()
    